
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"Source IP: {src_ip}  Destination IP: {dst_ip}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"Source Port: {src_port}  Destination Port: {dst_port}")

        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"Source Port: {src_port}  Destination Port: {dst_port}")

def main():
    packets = sniff(filter="tcp or udp", count=10)
    
    for packet in packets:
        analyze_packet(packet)

if __name__ == "__main__":
    main()
