
from scapy.all import *

# Creating a packet counter
packet_counter = 0

# Function to analyze packets
def analyze_packet(packet):
    global packet_counter
    packet_counter += 1
    print(f"Packet #{packet_counter}: {packet.summary()}")

# Sniffing network traffic
sniff(prn=analyze_packet, count=10)
