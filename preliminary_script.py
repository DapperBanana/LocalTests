
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1

given_number = int(input("Enter a number: "))
result = next_prime(given_number)
print(f"The smallest prime number greater than {given_number} is {result}")
