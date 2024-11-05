
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(num):
    prime = num + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1

num = int(input("Enter a number: "))
next_prime_num = next_prime(num)
print(f"The smallest prime number greater than {num} is: {next_prime_num}")
