
from scapy.all import *

# Define a function to analyze the packets
def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

# Sniff the network traffic and call the analyze_packet function for each packet
sniff(filter="tcp", prn=analyze_packet, count=10)
