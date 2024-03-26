
def is_vampire_number(n):
    n_str = str(n)
    
    # Check if number of digits is even
    if len(n_str) % 2 != 0:
        return False

    # Check all possible combinations of two factors
    for i in range(10**(len(n_str)//2)):
        for j in range(10**(len(n_str)//2)):
            if i * j == n:
                factor_str = str(i) + str(j)
                if ''.join(sorted(factor_str)) == ''.join(sorted(n_str)):
                    return True

    return False

# Test the program
num = 1260
if is_vampire_number(num):
    print(f"{num} is a vampire number")
else:
    print(f"{num} is not a vampire number")
