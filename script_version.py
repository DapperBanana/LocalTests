
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    total = 0
    for i in range(start, end + 1):
        if is_prime(i):
            total += i
    return total

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

sum_of_primes_in_range = sum_of_primes(start_range, end_range)

print("The sum of all prime numbers in the range {} to {} is: {}".format(start_range, end_range, sum_of_primes_in_range))
