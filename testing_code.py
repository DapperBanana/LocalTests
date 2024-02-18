
from scapy.all import *

def analyze_packet(packet):
    print(packet.summary())
    if IP in packet:
        print("Source IP: ", packet[IP].src)
        print("Destination IP: ", packet[IP].dst)
    if TCP in packet:
        print("Source Port: ", packet[TCP].sport)
        print("Destination Port: ", packet[TCP].dport)
    if DNS in packet:
        print("DNS Query: ", packet[DNS].qd.qname.decode("utf-8"))

def sniff_traffic(interface="eth0"):
    sniff(iface=interface, prn=analyze_packet)

if __name__ == "__main__":
    sniff_traffic()
