
def prime_factors(num):
    factors = []
    divisor = 2
    
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    
    return factors

num = int(input("Enter a number: "))
print("Prime factors of", num, "are:", prime_factors(num))
