
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_numbers(start, end):
    count = 0
    for i in range(start, end+1):
        if is_prime(i):
            count += 1
    return count

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print("Number of prime numbers in the range from {} to {} is: {}".format(start, end, count_prime_numbers(start, end)))
