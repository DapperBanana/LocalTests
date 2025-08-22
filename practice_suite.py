
import scapy.all as scapy

# Function to analyze network traffic
def analyze_traffic(packet):
    if packet.haslayer(scapy.IP):
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst

        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

# Sniff network traffic
scapy.sniff(prn=analyze_traffic, store=False)
