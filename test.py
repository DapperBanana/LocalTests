
import re

def is_valid_ipv4(ip):
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False

ip_address = input("Enter an IPv4 address: ")
if is_valid_ipv4(ip_address):
    print("The entered IP address is a valid IPv4 address.")
else:
    print("The entered IP address is not a valid IPv4 address.")
