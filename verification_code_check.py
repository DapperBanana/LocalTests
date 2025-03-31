
import re

def is_valid_ipv6_address(ip):
    pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
    if pattern.match(ip):
        return True
    else:
        return False

ip_address = input("Enter an IPv6 address: ")
if is_valid_ipv6_address(ip_address):
    print(f"{ip_address} is a valid IPv6 address.")
else:
    print(f"{ip_address} is not a valid IPv6 address.")
