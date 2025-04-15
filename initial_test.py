
def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False

    return True

ip_address = input("Enter an IPv4 address: ")
if is_valid_ipv4(ip_address):
    print("The provided IP address is valid.")
else:
    print("The provided IP address is not valid.")
