
import socket

def is_valid_ipv4_address(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False

ip_address = input("Enter an IPv4 address: ")
if is_valid_ipv4_address(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
