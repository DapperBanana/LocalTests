
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"IP Packet: Source IP = {src_ip}, Destination IP = {dst_ip}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"TCP Packet: Source Port = {src_port}, Destination Port = {dst_port}")

    if UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
        print(f"UDP Packet: Source Port = {src_port}, Destination Port = {dst_port}")

def capture_packets():
    sniff(prn=analyze_packet, filter="tcp or udp", count=10)

if __name__ == "__main__":
    capture_packets()

