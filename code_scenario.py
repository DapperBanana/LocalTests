
def get_prime_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number: "))
prime_factors = get_prime_factors(number)
print("Prime factors of", number, "are:", prime_factors)
