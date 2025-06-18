
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_numbers(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

count = count_prime_numbers(start, end)
print(f"The number of prime numbers in the range {start} to {end} is: {count}")
