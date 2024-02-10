
from scapy.all import *

def packet_analyzer(packet):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"TCP Packet: {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

    elif packet.haslayer(UDP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        print(f"UDP Packet: {src_ip}:{src_port} --> {dst_ip}:{dst_port}")

    elif packet.haslayer(ICMP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        icmp_type = packet[ICMP].type
        icmp_code = packet[ICMP].code

        print(f"ICMP Packet: {src_ip} --> {dst_ip} Type: {icmp_type} Code: {icmp_code}")

# Sniff network traffic
sniff(prn=packet_analyzer, filter="tcp or udp or icmp")
