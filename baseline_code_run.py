
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

print("Number of prime numbers in the range:", count_primes(start_range, end_range))
