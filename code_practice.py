
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(limit):
    prime_sum = 0
    for i in range(2, limit + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum

limit = int(input("Enter the limit: "))
total_prime_sum = prime_sum(limit)
print(f"The sum of all prime numbers up to {limit} is: {total_prime_sum}")
