
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end):
        if is_prime(num):
            count += 1
    return count

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Number of prime numbers in the range is:", count_primes(start, end))
