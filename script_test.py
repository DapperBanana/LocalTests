
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

result = sum_of_primes(start, end)
print(f"The sum of all prime numbers between {start} and {end} is: {result}")
