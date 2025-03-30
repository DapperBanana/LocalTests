
def is_perfect_square(num):
    if num < 0:
        return False
    
    if num == 0:
        return True
    
    x = num // 2
    seen = set([x])
    
    while x * x != num:
        x = (x + (num // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    
    return True

# Test the function with some examples
print(is_perfect_square(16))  # True
print(is_perfect_square(25))  # True
print(is_perfect_square(10))  # False
print(is_perfect_square(-1))  # False
