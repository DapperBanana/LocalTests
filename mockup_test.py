
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(start, end):
    sum_primes = 0
    for num in range(start, end + 1):
        if is_prime(num):
            sum_primes += num
    return sum_primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_of_primes(start, end)
print(f"The sum of all prime numbers in the range {start} to {end} is: {result}")
