
from scapy.all import *

def analyze_traffic(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"IP source: {ip_src} --> IP destination: {ip_dst}")

    if TCP in packet:
        tcp_sport = packet[TCP].sport
        tcp_dport = packet[TCP].dport
        print(f"TCP source port: {tcp_sport} --> TCP destination port: {tcp_dport}")

def capture_traffic(iface):
    sniff(iface=iface, prn=analyze_traffic)

if __name__ == '__main__':
    iface = input("Enter the interface to capture traffic on: ")
    capture_traffic(iface)
