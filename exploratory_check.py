
from scapy.all import *


def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"Source Port: {src_port}")
        print(f"Destination Port: {dst_port}")

    print("\n")


def main():
    print("Analyzing network traffic...")
    sniff(prn=analyze_packet, count=10)


if __name__ == "__main__":
    main()
