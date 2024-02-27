
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = 0
    for number in range(start, end+1):
        if is_prime(number):
            prime_sum += number
    return prime_sum

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print(f"The sum of all prime numbers between {start_range} and {end_range} is: {sum_of_primes(start_range, end_range)}")
