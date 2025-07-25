
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    total = 0
    for i in range(start, end + 1):
        if is_prime(i):
            total += i
    return total

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

result = sum_of_primes(start, end)
print(f"The sum of prime numbers in the range {start} to {end} is: {result}")
