
def is_valid_ipv4(address):
    parts = address.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False

    return True

address = input("Enter an IPv4 address: ")
if is_valid_ipv4(address):
    print(address, "is a valid IPv4 address.")
else:
    print(address, "is not a valid IPv4 address.")
