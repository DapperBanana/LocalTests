
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        print("IP Packet: {}".format(packet[IP].src))
    elif TCP in packet:
        print("TCP Packet: Source Port - {}, Destination Port - {}".format(packet[TCP].sport, packet[TCP].dport))
    elif UDP in packet:
        print("UDP Packet: Source Port - {}, Destination Port - {}".format(packet[UDP].sport, packet[UDP].dport))
    else:
        print("Unknown Packet Type")

def packet_callback(packet):
    analyze_packet(packet)

sniff(prn=packet_callback, count=10)
