# Network Traffic Visualization

**Network Traffic Visualization** is a Python-based tool designed to analyze network traffic captured in `.pcap` files and visualize IP communication geographically using KML (Keyhole Markup Language). The project helps users understand the origin and destination of network traffic, classify IP addresses, and map them using GeoIP data.

---

## Features

* **Packet Analysis:** Parses `.pcap` files and extracts relevant network data using `dpkt`.
* **IP Classification:** Differentiates between private, public, and multicast IPs.
* **Geo Mapping:** Maps IP addresses to geographic locations using the GeoLiteCity database.
* **KML Generation:** Generates KML files compatible with Google Earth or Maps for visual analysis.
* **Modular Architecture:** Easily extendable for advanced applications such as Intrusion Detection Systems (IDS).

---

## Technical Stack

| Component       | Technology Used          |
| --------------- | ------------------------ |
| Packet Analysis | Python, dpkt, Wireshark  |
| Geolocation     | pygeoip, GeoLiteCity.dat |
| Visualization   | KML, Google Earth        |
| Programming     | Python 3.8+              |

---

## Getting Started

### Prerequisites

* Python 3.8 or higher
* Wireshark (for capturing `.pcap` files)
* [GeoLiteCity Database](https://dev.maxmind.com/geoip/geoip2/geolite2/)

  * Place `GeoLiteCity.dat` in the root directory of the project.

### Installation

```bash
git clone https://github.com/saadali112/Network-traffic-visualization.git
cd Network-traffic-visualization
pip install -r requirements.txt
```

### Usage

1. Capture network traffic using Wireshark and save it as a `.pcap` file.
2. Place the `.pcap` file in the project root directory.
3. Run the script:

```bash
python3 main.py <your_file.pcap>
```

4. Open the generated `output.kml` file with Google Earth or any KML viewer.

---

## IP Address Categories

* **Private IPs:** Local network addresses (e.g., 192.168.x.x, 10.x.x.x)
* **Public IPs:** Routable addresses on the internet
* **Multicast IPs:** Used for broadcasting in subnetworks

> The tool automatically identifies and filters these categories for visualization.

---

## Sample Output

* Displays geographic origin and destination of network packets.
* Can be extended to highlight potentially malicious activity or suspicious traffic patterns.

---

## Use Cases

* Educational demonstrations in networking and cybersecurity.
* Basic network forensics and traffic analysis.
* Geographical traffic visualization for SIEM dashboards.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for improvements, additional features, or bug fixes.
