
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Src IP: {src_ip} Dst IP: {dst_ip} Protocol: {protocol}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"Src Port: {src_port} Dst Port: {dst_port}")

    if UDP in packet:
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        print(f"Src Port: {src_port} Dst Port: {dst_port}")

def main():
    packets = rdpcap('network_traffic.pcap')  # Load network traffic from a pcap file

    for packet in packets:
        analyze_packet(packet)

if __name__ == "__main__":
    main()
