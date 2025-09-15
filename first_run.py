
from scapy.all import sniff, IP

def analyze_traffic(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

# Sniff network traffic and call analyze_traffic function for each packet
sniff(prn=analyze_traffic, store=0)
