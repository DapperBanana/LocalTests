
import re

def is_valid_ipv6(ip):
    pattern = re.compile(
        r'^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$'
    )
    if pattern.match(ip):
        return True
    else:
        return False

# Test the function with some sample inputs
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # True
print(is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334:"))  # False
print(is_valid_ipv6("2001:0db8:85a3::8a2e:0370:7334"))  # False
print(is_valid_ipv6("::1"))  # True
