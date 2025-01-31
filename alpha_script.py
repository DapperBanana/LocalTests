
from scapy.all import *

def analyze_traffic(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        print(f"Source IP: {src_ip} --> Destination IP: {dst_ip}")

    if TCP in pkt:
        src_port = pkt[TCP].sport
        dst_port = pkt[TCP].dport
        print(f"Source Port: {src_port} --> Destination Port: {dst_port}")

    if HTTP in pkt:
        http_request = pkt[HTTP].Request
        print(f"HTTP Request: {http_request}")

def main():
    sniff(prn=analyze_traffic, count=10)  # Analyze first 10 packets

if __name__ == "__main__":
    main()
