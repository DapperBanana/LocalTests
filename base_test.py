
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1

given_number = int(input("Enter a number: "))
next_prime_number = next_prime(given_number)

print(f"The smallest prime number greater than {given_number} is {next_prime_number}")
