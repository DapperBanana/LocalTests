
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

num = int(input("Enter a number: "))
next_prime = find_next_prime(num)
print(f"The smallest prime number greater than {num} is {next_prime}")
