
import re

def is_valid_ipv6(ipv6):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    if re.match(pattern, ipv6):
        return True
    else:
        return False

ipv6_address = input("Enter an IPv6 address: ")

if is_valid_ipv6(ipv6_address):
    print("The input is a valid IPv6 address.")
else:
    print("The input is not a valid IPv6 address.")
