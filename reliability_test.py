
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

given_number = int(input("Enter a number: "))
next_prime = find_next_prime(given_number)
print(f"The smallest prime number greater than {given_number} is: {next_prime}")
