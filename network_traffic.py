import dpkt
import socket
import pygeoip

gi = pygeoip.GeoIP('GeoLiteCity.dat')  # Ensure the path to GeoLiteCity.dat is correct

def main():
    try:
        f = open('wire.pcap', 'rb')
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    pcap = dpkt.pcap.Reader(f)
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
                '<Style id="transBluePoly">' \
                '<LineStyle>' \
                '<width>1.5</width>' \
                '<color>501400E6</color>' \
                '</LineStyle>' \
                '</Style>'
    kmlfooter = '</Document>\n</kml>\n'

    # Generate KML content by plotting the IPs
    kmldoc = kmlheader + plotIPs(pcap) + kmlfooter
    print(kmldoc)  # Print the KML document for debugging

    # Write the KML content to a file
    with open('file.kml', 'w') as f:
        f.write(kmldoc)

def plotIPs(pcap):
    kmlPts = ''
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)  # Decode Ethernet frame
            ip = eth.data  # Extract IP layer data
            if isinstance(ip, dpkt.ip.IP):  # Ensure it's an IP packet
                src = socket.inet_ntoa(ip.src)  # Convert source IP to string
                dst = socket.inet_ntoa(ip.dst)  # Convert destination IP to string

                # Debugging: Print the source and destination IPs
                print(f"Extracted IPs: Source={src}, Destination={dst}")
                
                KML = retKML(dst, src)  # Generate KML for each pair of IPs
                kmlPts = kmlPts + KML  # Append the generated KML
        except Exception as e:
            print(f"Error processing packet: {e}")
            pass

    return kmlPts

def retKML(dstip, srcip):
    try:
        dst = gi.record_by_name(dstip)  # Get geolocation for destination IP
        if dst is None:
            print(f"No geolocation found for destination IP: {dstip}")
            return ''  # Return empty string if no location is found
        
        src = gi.record_by_name(srcip)  # Get geolocation for source IP
        if src is None:
            print(f"No geolocation found for source IP: {srcip}")
            return ''  # Return empty string if no location is found
        
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']

        # Create KML placemark for the line connecting the source and destination
        kml = (
            '<Placemark>\n'
            '<name>%s to %s</name>\n'
            '<extrude>1</extrude>\n'
            '<tessellate>1</tessellate>\n'
            '<styleUrl>#transBluePoly</styleUrl>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (srcip, dstip, srclongitude, srclatitude, dstlongitude, dstlatitude)

        return kml
    except Exception as e:
        print(f"Error processing geolocation for {dstip} and {srcip}: {e}")
        return ''  # Return an empty string if there's an error

if __name__ == '__main__':
    main()
