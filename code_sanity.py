
import re

def is_valid_ipv6(ipv6):
    pattern = re.compile(r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4})$')
    if pattern.match(ipv6):
        return True
    else:
        return False

# Test the function
ipv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
print(is_valid_ipv6(ipv6))  # Output: True

ipv6 = "2001:0db8:85a3::8A2E:037j:7334"
print(is_valid_ipv6(ipv6))  # Output: False
