
import ipaddress

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

ip = input("Enter an IP address: ")
if is_valid_ipv4(ip):
    print(f"{ip} is a valid IPv4 address.")
else:
    print(f"{ip} is not a valid IPv4 address.")
