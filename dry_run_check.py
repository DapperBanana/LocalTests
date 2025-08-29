
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        print("IP packet:")
        print(packet.show())
    elif TCP in packet:
        print("TCP packet:")
        print(packet.show())
    elif UDP in packet:
        print("UDP packet:")
        print(packet.show())

def capture_traffic():
    sniff(prn=analyze_packet, count=10)

if __name__ == "__main__":
    capture_traffic()
