
def is_vampire_number(num):
    num_str = str(num)
    num_len = len(num_str)
    
    if num_len % 2 != 0:
        return False

    for i in range(10**(num_len//2 - 1), int(num**0.5)+1):
        if num % i == 0:
            j = num / i
            if sorted(str(i) + str(j)) == sorted(num_str):
                return True
    
    return False

# Test the function with some examples
print(is_vampire_number(1260))  # True
print(is_vampire_number(1122))  # False
print(is_vampire_number(321))   # False
