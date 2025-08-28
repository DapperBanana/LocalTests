
from scapy.all import *

# Define a function to analyze the network traffic
def analyze_traffic(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

# Capture network traffic
sniff(prn=analyze_traffic, count=10)
