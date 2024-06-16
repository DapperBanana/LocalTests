
import re

def is_valid_ipv6(address):
    pattern = re.compile("^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    return bool(pattern.match(address))

address = input("Enter IPv6 address: ")
if is_valid_ipv6(address):
    print("Valid IPv6 address")
else:
    print("Invalid IPv6 address")
