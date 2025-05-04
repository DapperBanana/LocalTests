
from scapy.all import sniff, IP

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")

# Sniff network traffic and call analyze_packet function for each packet
sniff(prn=analyze_packet, count=10)
