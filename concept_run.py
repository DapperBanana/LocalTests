
from scapy.all import *

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")

def sniff_traffic(interface, count):
    sniff(iface=interface, prn=analyze_packet, count=count)

if __name__ == "__main__":
    interface = "eth0" # Change this to your network interface
    count = 10 # Number of packets to capture
    sniff_traffic(interface, count)
