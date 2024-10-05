
from scapy.all import *

# Function to analyze network traffic
def analyze_traffic(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"SRC IP: {src_ip} DST IP: {dst_ip} PROTOCOL: {protocol}")

# Sniff network traffic
sniff(prn=analyze_traffic, count=10)
