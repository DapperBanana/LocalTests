
def get_prime_factors(number):
    prime_factors = []
    factor = 2

    while factor * factor <= number:
        if number % factor:
            factor += 1
        else:
            number //= factor
            prime_factors.append(factor)
    
    if number > 1:
        prime_factors.append(number)

    return prime_factors

# Input number
num = int(input("Enter a number: "))

print(f"The prime factors of {num} are: {get_prime_factors(num)}")
