
def is_vampire_number(num):
    num_str = str(num)
    num_len = len(num_str)

    if num_len % 2 != 0:
        return False

    num_digits = [int(d) for d in num_str]
    num_digits.sort()

    for i in range(10**(num_len//2), int(num**0.5)+1):
        if num % i == 0:
            factors = [int(d) for d in str(i) + str(num // i)]
            factors.sort()
            if factors == num_digits:
                return True

    return False

# Test the function
num = 1260
if is_vampire_number(num):
    print(f"{num} is a vampire number.")
else:
    print(f"{num} is not a vampire number.")
