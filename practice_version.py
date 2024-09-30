
from scapy.all import *

def analyze_packet(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        print(f"IP Packet: {src_ip} -> {dst_ip}")

    if packet.haslayer(TCP):
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"TCP Packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

def main():
    pcap_file = "network_traffic.pcap"
    packets = rdpcap(pcap_file)

    for packet in packets:
        analyze_packet(packet)

if __name__ == "__main__":
    main()
