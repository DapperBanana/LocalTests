
from scapy.all import *

# Function to analyze network traffic
def analyze_traffic(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")

# Sniff network traffic
sniff(prn=analyze_traffic, count=10)
