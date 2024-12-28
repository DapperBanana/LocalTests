
import socket

def is_valid_ipv4(ip_str):
    try:
        socket.inet_pton(socket.AF_INET, ip_str)
        return True
    except:
        return False

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print("The IPv4 address {} is valid.".format(ip_address))
else:
    print("The IPv4 address {} is not valid.".format(ip_address))
