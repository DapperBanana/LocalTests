
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit):
    sum_primes = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes

limit = int(input("Enter a limit: "))
result = sum_primes(limit)
print(f"The sum of all prime numbers up to {limit} is: {result}")
