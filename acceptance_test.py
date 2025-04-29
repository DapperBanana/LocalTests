
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num

given_number = int(input("Enter a number: "))
result = next_prime(given_number)
print(f"The smallest prime number greater than {given_number} is: {result}")
