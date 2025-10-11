
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
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
print(f"The sum of all prime numbers between {start} and {end} is: {result}")
