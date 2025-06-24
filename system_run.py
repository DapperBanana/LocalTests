
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    if start > end:
        return 0
    total_sum = 0
    for i in range(start, end+1):
        if is_prime(i):
            total_sum += i
    return total_sum

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"The sum of all prime numbers in the range {start} to {end} is: {sum_of_primes(start, end)}")
