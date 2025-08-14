
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    prime_sum = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum

limit = int(input("Enter a limit: "))
result = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is: {result}")
