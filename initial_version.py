
from scapy.all import *

def analyze_packets(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"Source Port: {src_port} --> Destination Port: {dst_port}")

    if Raw in packet:
        data = packet[Raw].load
        print(f"Data: {data}")

def main():
    pcap_file = "network_traffic.pcap"
    packets = rdpcap(pcap_file)

    for packet in packets:
        analyze_packets(packet)

if __name__ == "__main__":
    main()
