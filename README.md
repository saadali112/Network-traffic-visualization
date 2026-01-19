
Network Traffic Visualization
📖 Overview
Network Traffic Visualization is a Python-based tool that enables users to analyze .pcap files captured via Wireshark and visualize IP traffic on a map using KML (Keyhole Markup Language). This helps users better understand where network traffic originates and terminates by identifying IP address types and mapping them using GeoIP data.

✨ Features
🔍 Packet Analysis: Parses .pcap files and extracts relevant data using dpkt.
🧠 IP Classification: Differentiates between private, public, and multicast IPs.
🌍 Geo Mapping: Maps IPs to geographic locations using the GeoLiteCity database.
🗺️ KML File Generation: Creates KML files that can be opened in Google Earth or Maps.
🧩 Modular Architecture: Easily extendable for advanced applications like intrusion detection systems (IDS).

🛠️ Technical Stack
Component	Technology Used
Packet Analysis	dpkt, Wireshark
Geolocation	pygeoip, GeoLiteCity.dat
Visualization	KML, Google Earth
Programming	Python 3.8+
🚀 Getting Started
✅ Prerequisites
Python 3.8 or above
Wireshark for packet capture
GeoLiteCity Database
Download and place GeoLiteCity.dat in the root directory of the project.

📦 Installation
git clone https://github.com/saadali112/Network-traffic-visualization.git
cd Network-traffic-visualization
pip install -r requirements.txt

📊 Usage
Capture network traffic using Wireshark and save it as a .pcap file.
Place the .pcap file in the project root.
Run the script with:
python3 main.py <your_file.pcap>
Open the generated output.kml with Google Earth or any KML viewer.
🔐 IP Address Categories
Private IPs: Local network addresses (e.g., 192.168.x.x, 10.x.x.x)
Public IPs: Routable addresses on the internet
Multicast IPs: Used for broadcasting in subnetworks
These categories are identified and filtered before visualization.

🧪 Sample Output
Displays geographic origin and destination of IP packets
Can be extended to highlight potentially malicious activity
📌 Use Cases
Educational demonstrations in networking and cybersecurity
Basic network forensics
Geographical traffic visualization for SIEM dashboards
