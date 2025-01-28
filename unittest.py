
import ipaddress

def is_valid_ipv6(address):
    try:
        ipaddress.IPv6Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

# Test the function
address1 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
address2 = "2001:0db8:85a3::8A2E:0370:7334"
address3 = "2001:0db8:85a3:00::8A2E:0370:7334"
address4 = "2001:0db8:85aZ:0000:0000:8a2e:0370:7334"

print(is_valid_ipv6(address1))  # True
print(is_valid_ipv6(address2))  # True
print(is_valid_ipv6(address3))  # True
print(is_valid_ipv6(address4))  # False
