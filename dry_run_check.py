
import re

def is_valid_ipv4(ip):
    pattern = re.compile(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
    match = pattern.match(ip)
    
    if not match:
        return False
    
    for octet in match.groups():
        if int(octet) > 255:
            return False
    
    return True

# Test the function
ip_address = "192.168.1.1"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address")
else:
    print(f"{ip_address} is not a valid IPv4 address")
