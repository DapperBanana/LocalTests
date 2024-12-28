
import socket

def is_valid_ipv6(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
        return True
    except socket.error:
        return False

address = input("Enter an IPv6 address: ")
if is_valid_ipv6(address):
    print("The address is a valid IPv6 address.")
else:
    print("The address is not a valid IPv6 address.")
