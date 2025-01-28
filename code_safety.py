
from scapy.all import *

# Function to analyze network traffic
def analyze_traffic(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"Source Port: {src_port} --> Destination Port: {dst_port}")

# Sniff network traffic
sniff(prn=analyze_traffic, count=10)
