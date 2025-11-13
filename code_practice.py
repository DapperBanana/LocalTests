
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        number += 1

given_number = int(input("Enter a number: "))
print(f"The smallest prime number greater than {given_number} is: {next_prime(given_number)}")
