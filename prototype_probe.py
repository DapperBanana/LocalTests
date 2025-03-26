
from scapy.all import *
from collections import Counter

def analyze_traffic(pcap_file):
    packets = rdpcap(pcap_file)
    
    src_ips = Counter()  # Counter to store source IPs and their counts
    dst_ips = Counter()  # Counter to store destination IPs and their counts

    for packet in packets:
        if IP in packet:
            src_ips[packet[IP].src] += 1
            dst_ips[packet[IP].dst] += 1

    print("Source IPs:")
    for ip, count in src_ips.items():
        print(f"{ip}: {count} packets")

    print("\nDestination IPs:")
    for ip, count in dst_ips.items():
        print(f"{ip}: {count} packets")

if __name__ == "__main__":
    pcap_file = "network_traffic.pcap"
    analyze_traffic(pcap_file)
