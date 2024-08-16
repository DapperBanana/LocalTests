
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
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

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

result = count_primes(start_range, end_range)
print("Number of prime numbers in the range:", result)
