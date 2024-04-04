
import re

def is_valid_ipv6(ipv6):
    pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$')
    return True if pattern.match(ipv6) else False

ipv6_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
if is_valid_ipv6(ipv6_address):
    print("Valid IPv6 address")
else:
    print("Invalid IPv6 address")
