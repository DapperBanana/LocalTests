
from scapy.all import *

# Create a function to analyze network traffic
def analyze_traffic(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

# Sniff network traffic and pass each packet to the analyze_traffic function
sniff(prn=analyze_traffic, filter="ip", count=10)
