
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1

given_num = int(input("Enter a number: "))
result = next_prime(given_num)
print("The smallest prime number greater than", given_num, "is:", result)
