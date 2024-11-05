
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_prime_numbers(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total_sum += num
    return total_sum

start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

sum_of_primes = sum_prime_numbers(start_range, end_range)

print(f"The sum of prime numbers in the range ({start_range}, {end_range}) is: {sum_of_primes}")
