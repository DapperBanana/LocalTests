
import re

def is_valid_ipv6_address(ip_address):
    ipv6_pattern = re.compile("^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", re.IGNORECASE)
    if re.match(ipv6_pattern, ip_address):
        return True
    else:
        return False

# Test the function
ip_address = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
if is_valid_ipv6_address(ip_address):
    print(f"{ip_address} is a valid IPv6 address.")
else:
    print(f"{ip_address} is not a valid IPv6 address.")
