
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))

result = sum_of_primes(start_range, end_range)
print(f"The sum of prime numbers in the range [{start_range}, {end_range}] is: {result}")
