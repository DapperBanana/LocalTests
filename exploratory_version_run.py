
def is_carmichael_number(n):
    # Check if n is a composite number
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    
    # Check if n is a Carmichael number
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            return False
    return True

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a Carmichael number
if is_carmichael_number(num):
    print(f"{num} is a Carmichael number.")
else:
    print(f"{num} is not a Carmichael number.")
