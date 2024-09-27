
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            total += num
    return total

limit = int(input("Enter a limit: "))
sum_primes = sum_of_primes(limit)

print(f"The sum of all prime numbers up to {limit} is: {sum_primes}")
