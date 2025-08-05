
import socket

def is_valid_ipv4(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print("The entered string is a valid IPv4 address.")
else:
    print("The entered string is not a valid IPv4 address.")
