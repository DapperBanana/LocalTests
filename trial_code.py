
from scapy.all import sniff, TCP

# Callback function to process packets
def packet_callback(packet):
    if TCP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        print(f"TCP packet from {src_ip}:{src_port} to {dst_ip}:{dst_port}")

# Sniff network traffic on interface 'eth0'
sniff(iface='eth0', prn=packet_callback, filter='tcp')

