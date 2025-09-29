
def is_vampire_number(num):
    num_str = str(num)
    if len(num_str) % 2 != 0:
        return False

    num_digits = [int(d) for d in str(num)]
    num_length = len(num_digits)

    for i in range(10 ** (num_length//2 - 1), int(num**0.5) + 1):
        if num % i == 0:
            j = num // i
            if sorted(str(i) + str(j)) == sorted(str(num)):
                return True

    return False

# Test the program with some vampire number
num1 = 1260
num2 = 1827

if is_vampire_number(num1):
    print(f"{num1} is a vampire number")
else:
    print(f"{num1} is not a vampire number")

if is_vampire_number(num2):
    print(f"{num2} is a vampire number")
else:
    print(f"{num2} is not a vampire number")
