
import re

def is_valid_ipv4(ip):
    ipv4_pattern = re.compile(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    
    if ipv4_pattern.match(ip):
        return True
    else:
        return False

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print("The IP address is valid.")
else:
    print("The IP address is not valid.")
