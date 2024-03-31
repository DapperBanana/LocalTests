
def is_lucas_carmichael(num):
    def lucas_sequence(n):
        a, b = 2, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    def power_mod(base, exp, mod):
        res = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % mod
            exp = exp // 2
            base = (base * base) % mod
        return res

    if num < 2:
        return False
    for i in lucas_sequence(num-1):
        if power_mod(i, num-1, num) != 1:
            return False
    return True

num = int(input("Enter a number to check if it is a Lucas-Carmichael number: "))
if is_lucas_carmichael(num):
    print(f"{num} is a Lucas-Carmichael number.")
else:
    print(f"{num} is not a Lucas-Carmichael number.")
