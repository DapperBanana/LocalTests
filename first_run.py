
def is_prime(number):
    # 1 and numbers less than 1 are not prime
    if number <= 1:
        return False

    # 2 is the only even prime number
    if number == 2:
        return True

    # Check if number is divisible by any number from 2 to the square root of number
    # If it is, then it is not prime
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    # If the loop finishes without finding any divisors, it is a prime number
    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
