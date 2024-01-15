
def prime_factors(n):
    factors = [] # store the prime factors
    
    # divide the number by 2 until it's no longer divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # check for the remaining prime factors
    i = 3
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # if n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors


# get input from the user
num = int(input("Enter a positive integer: "))

# find the prime factors
factors = prime_factors(num)

# display the prime factors
print("Prime factors of", num, "are:", factors)
