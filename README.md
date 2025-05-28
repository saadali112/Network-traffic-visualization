# Network Traffic Visualization Project


## 📌 Project Overview
A Python-based tool that analyzes network traffic using Wireshark captures, classifies IP addresses, and visualizes geographic locations on Google Maps via KML generation.

## ✨ Key Features
- **Packet Analysis**: Captures and processes `.pcap` files using Wireshark
- **IP Classification**: Identifies public/private/multicast IPs
- **Geo-Mapping**: Visualizes traffic flows with GeoIP coordinates
- **KML Generation**: Creates interactive maps for Google Earth
- **Modular Design**: Easily extendable for intrusion detection systems

## 🛠️ Technical Stack
| Component       | Technology Used          |
|-----------------|--------------------------|
| Packet Analysis | Wireshark, dpkt          |
| Geolocation     | pygeoip, GeoLiteCity     |
| Visualization   | KML/Google Maps          |
| Core Language   | Python 3.8+              |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Wireshark (for packet capture)
- [GeoLiteCity Database](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) (Place in project root)

- 🤝## How to Contribute
Fork the repository

Create a feature branch (git checkout -b feature/your-feature)

Commit changes (git commit -m 'Add feature')

Push to branch (git push origin feature/your-feature)

Open a Pull Request

### Installation
```bash
git clone https://github.com/saadali112/Network-traffic-visualization.git
cd Network-traffic-visualization
pip install -r requirements.txt




