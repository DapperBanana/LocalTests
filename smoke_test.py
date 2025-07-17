
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    sum_primes = 0
    for i in range(start, end + 1):
        if is_prime(i):
            sum_primes += i
    return sum_primes

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

total_sum = sum_of_primes(start_range, end_range)
print(f"The sum of all prime numbers in the range from {start_range} to {end_range} is: {total_sum}")
