
from scapy.all import *

# Define a callback function to handle each packet
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"IP Packet: {src_ip} -> {dst_ip} Protocol: {protocol}")

# Set the network interface to sniff traffic on
interface = "en0"
print(f"Sniffing on interface {interface}...")

# Start sniffing packets
sniff(iface=interface, prn=packet_callback, store=0)
