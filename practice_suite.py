
from scapy.all import *

# Define a function to analyze and print network traffic
def analyze_traffic(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"SRC IP: {src_ip} --> DST IP: {dst_ip}")

# Sniff network traffic and analyze packets
sniff(prn=analyze_traffic, count=10)
