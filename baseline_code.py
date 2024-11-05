
import re

def is_valid_ipv6(address):
    pattern = re.compile('^([0-9a-f]{1,4}:){7}([0-9a-f]{1,4})$', re.IGNORECASE)
    if pattern.match(address):
        return True
    else:
        return False

# Test the function
address1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
address2 = "2001:0db8:85a3::8a2e:0370:7334"
address3 = "2001:0db8:85a3:0000:0000:8a2e:0370"
address4 = "200.hello.world"
address5 = "1234:abcd"

print(is_valid_ipv6(address1))  # True
print(is_valid_ipv6(address2))  # True
print(is_valid_ipv6(address3))  # False
print(is_valid_ipv6(address4))  # False
print(is_valid_ipv6(address5))  # False
