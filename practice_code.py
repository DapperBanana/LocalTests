
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_numbers(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

num_primes = count_prime_numbers(start_range, end_range)

print(f"There are {num_primes} prime numbers in the range {start_range}-{end_range}")
