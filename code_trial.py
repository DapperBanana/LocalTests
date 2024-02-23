
import ipaddress

def is_valid_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

ip = input("Enter an IPv6 address: ")

if is_valid_ipv6(ip):
    print(f"{ip} is a valid IPv6 address.")
else:
    print(f"{ip} is not a valid IPv6 address.")
