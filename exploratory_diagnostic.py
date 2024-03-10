
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

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

prime_count = count_primes(start, end)
print(f"The number of prime numbers in the range [{start}, {end}] is {prime_count}")
