
def power_mod(base, exponent, modulo):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        exponent = exponent >> 1
    return result

def is_carmichael_number(n):
    if n < 2 or n % 2 == 0:
        return False
        
    for a in range(2, n):
        if power_mod(a, n-1, n) != 1:
            return False

    return True

# Example usage
num = int(input("Enter a number: "))
if is_carmichael_number(num):
    print(num, "is a Carmichael number")
else:
    print(num, "is not a Carmichael number")
