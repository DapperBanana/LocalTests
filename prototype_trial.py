
import re

def is_valid_ipv6(ipv6):
    pattern = re.compile('^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$')
    if pattern.match(ipv6):
        return True
    else:
        return False

ipv6_address = input("Enter an IPv6 address: ")
if is_valid_ipv6(ipv6_address):
    print("Valid IPv6 address")
else:
    print("Invalid IPv6 address")
