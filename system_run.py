
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total_sum = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            total_sum += num
    return total_sum

limit = int(input("Enter a limit: "))
result = sum_of_primes(limit)
print(f"The sum of all prime numbers up to {limit} is: {result}")
