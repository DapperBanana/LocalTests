
import socket

def is_valid_ipv4(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip_address = "192.168.1.1"

if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
