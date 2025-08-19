
from scapy.all import *

def print_packet(packet):
    print(packet.summary())

def analyze_traffic(packet):
    if IP in packet:
        print("IP Packet:")
        print_packet(packet)
    elif TCP in packet:
        print("TCP Packet:")
        print_packet(packet)
    elif UDP in packet:
        print("UDP Packet:")
        print_packet(packet)
    else:
        print("Other Packet:")
        print_packet(packet)

def main():
    packets = sniff(count=10)  # Capture first 10 packets
    for packet in packets:
        analyze_traffic(packet)

if __name__ == "__main__":
    main()
