
from scapy.all import *

def analyze_traffic(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Source Port: {src_port} --> Destination Port: {dst_port}")

            data = packet[TCP].payload
            print(f"Data: {data}")

def main():
    sniff(prn=analyze_traffic, count=10)

if __name__ == "__main__":
    main()
