
from scapy.all import *

def analyze_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")

    if packet.haslayer(TCP):
        tcp_src = packet[TCP].sport
        tcp_dst = packet[TCP].dport
        print(f"TCP Packet: {tcp_src} -> {tcp_dst}")

    if packet.haslayer(UDP):
        udp_src = packet[UDP].sport
        udp_dst = packet[UDP].dport
        print(f"UDP Packet: {udp_src} -> {udp_dst}")

    if packet.haslayer(ICMP):
        icmp_type = packet[ICMP].type
        icmp_code = packet[ICMP].code
        print(f"ICMP Packet: Type {icmp_type}, Code {icmp_code}")

# Sniff network traffic on a specific interface (e.g. "eth0") for a certain number of packets
sniff(iface="eth0", count=10, prn=analyze_packet)
