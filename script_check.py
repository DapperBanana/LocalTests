
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end+1):
        if is_prime(num):
            count += 1
    return count

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

print("Number of prime numbers in the given range:", count_primes(start, end))
