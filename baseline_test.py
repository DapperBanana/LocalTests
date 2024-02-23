
from scapy.all import *

def analyze_traffic(pkt):
    if IP in pkt:
        print("Source IP: " + pkt[IP].src)
        print("Destination IP: " + pkt[IP].dst)
    if TCP in pkt:
        print("Source Port: " + str(pkt[TCP].sport))
        print("Destination Port: " + str(pkt[TCP].dport))

def main():
    sniff(prn=analyze_traffic, count=10)  # Sniff 10 packets and call analyze_traffic for each packet

if __name__ == "__main__":
    main()
