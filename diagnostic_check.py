
from scapy.all import *

# Function to analyze network traffic
def analyze_traffic(pkt):
    if IP in pkt:
        # Print source and destination IP addresses
        print("Source IP: ", pkt[IP].src)
        print("Destination IP: ", pkt[IP].dst)
        
        # Check if packet is TCP
        if TCP in pkt:
            # Print source and destination port numbers
            print("Source Port: ", pkt[TCP].sport)
            print("Destination Port: ", pkt[TCP].dport)
            
            # Print TCP flags
            print("TCP Flags: ")
            flags = pkt[TCP].flags
            if flags & 0x01:
                print("FIN")
            if flags & 0x02:
                print("SYN")
            if flags & 0x04:
                print("RST")
            if flags & 0x08:
                print("PSH")
            if flags & 0x10:
                print("ACK")
            if flags & 0x20:
                print("URG")
            if flags & 0x40:
                print("ECE")
            if flags & 0x80:
                print("CWR")
        
        print("-----")

# Sniff network traffic and call analyze_traffic function for each packet
sniff(prn=analyze_traffic)
