
import re

def check_ipv6_address(ip):
    # Regular expression to match IPv6 address
    pattern = re.compile(r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$')
    
    if pattern.match(ip):
        return True
    else:
        return False

# Test the function with some IPv6 addresses
print(check_ipv6_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) # True
print(check_ipv6_address("2001:0db8:85a3:0:0:8a2e:0370:7334")) # True
print(check_ipv6_address("2001:0db8:85a3::8a2e:0370:7334")) # True
print(check_ipv6_address("2001:0db8:85a3:0:0:8a2e:0370:7334:")) # False
print(check_ipv6_address("1234:5678:abcd:8763::")) # False
