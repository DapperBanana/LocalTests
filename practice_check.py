
import re

def is_valid_ipv4(ip):
    regex_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if re.match(regex_pattern, ip):
        return True
    else:
        return False

ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")
