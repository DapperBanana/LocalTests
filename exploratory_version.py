
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    sum_primes = 0
    for num in range(start, end + 1):
        if is_prime(num):
            sum_primes += num
    return sum_primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = sum_of_primes(start_range, end_range)
print(f"The sum of all prime numbers in the range {start_range} to {end_range} is: {result}")
