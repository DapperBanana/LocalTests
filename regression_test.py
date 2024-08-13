
import re

def validate_ipv6(ip):
    ipv6_pattern = re.compile('^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

    if ipv6_pattern.match(ip):
        return True
    else:
        return False

# Test the function with some sample IPv6 addresses
ips = ["2001:0db8:85a3:0000:0000:8a2e:0370:7334", "2001:0db8:85a3:0:0:8a2e:370:7334", "2001:db8:85a3:0:0:8a2e:370:7334", "2001:0db8:85a3::8a2e:0370:7334", "2001:0db8:85a3::8a2e:370:7334", "2001:0db8:85a3::8a2e:370:7334:"]

for ip in ips:
    if validate_ipv6(ip):
        print(f"{ip} is a valid IPv6 address")
    else:
        print(f"{ip} is not a valid IPv6 address")
