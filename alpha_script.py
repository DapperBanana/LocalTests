
import re

def is_valid_ipv6(ip):
    pattern = r"^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$"
    
    if re.match(pattern, ip):
        return True
    else:
        return False

ip = input("Enter an IPv6 address: ")
if is_valid_ipv6(ip):
    print("Valid IPv6 address")
else:
    print("Invalid IPv6 address")
