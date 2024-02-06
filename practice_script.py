
import re

def is_ipv6_address(address):
    # Regular expression pattern for valid IPv6 address
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    
    # Check if the address matches the pattern
    if re.match(pattern, address):
        return True
    else:
        return False

# Test the function
address1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
address2 = "2001:0db8:85a3::8a2e:0370:7334"
address3 = "2001:0db8:85a3:0000:0000:::0370:7334"

print(is_ipv6_address(address1))  # Output: True
print(is_ipv6_address(address2))  # Output: True
print(is_ipv6_address(address3))  # Output: False
