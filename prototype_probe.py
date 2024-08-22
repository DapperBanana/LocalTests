
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            total += i
    return total

limit = int(input("Enter a limit to calculate the sum of all prime numbers up to that limit: "))
print(f"The sum of all prime numbers up to {limit} is: {sum_of_primes(limit)}")
