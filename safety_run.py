
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total_sum = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            total_sum += i
    return total_sum

limit = int(input("Enter a limit to calculate the sum of all prime numbers up to that limit: "))
result = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is: {result}")
