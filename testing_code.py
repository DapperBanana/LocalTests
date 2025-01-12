
from scapy.all import *

# Create a packet callback function
def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

# Sniff network traffic and call the packet_callback function for each packet
sniff(prn=packet_callback, count=10)  # Change count=10 to sniff for a specific number of packets

