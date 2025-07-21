
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

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = sum_of_primes(start_range, end_range)
print(f"The sum of all prime numbers in the range {start_range} to {end_range} is: {result}")
