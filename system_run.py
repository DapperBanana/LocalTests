
import re

def is_valid_ipv6(ip):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$'
    if re.match(pattern, ip):
        return True
    else:
        return False

# Test the program with some IPv6 addresses
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) # True
print(is_valid_ipv6("fe80::a6db:6ff:feac:936")) # True
print(is_valid_ipv6("2001:0db8:85a3::8a2e:370:7334")) # False
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334:")) # False
