
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"The number of prime numbers in the range {start} to {end} is: {count_primes_in_range(start, end)}")
