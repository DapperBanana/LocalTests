
def is_perfect_digital_invariant(num):
    num_str = str(num)
    length = len(num_str)
    
    for i in range(length):
        digit = int(num_str[i])
        occurences = num_str.count(str(i))
        if digit != occurences:
            return False
    
    return True

# Test the function
num = 1210
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant")
else:
    print(f"{num} is not a perfect digital invariant")
