
from scapy.all import *


def analyze_traffic(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"IP Packet: {src_ip} => {dst_ip}")

    if TCP in packet:
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"TCP Packet: {src_port} => {dst_port}")


def main():
    print("Analyzing network traffic...")
    sniff(prn=analyze_traffic, count=10)


if __name__ == "__main__":
    main()
