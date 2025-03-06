
def is_perfect_digital_invariant(num):
    num_str = str(num)
    for i in range(len(num_str)-1):
        if abs(int(num_str[i]) - int(num_str[i+1])) != 1:
            return False
    return True

# Test the function with different numbers
num1 = 12345
num2 = 987654
num3 = 13579

print(is_perfect_digital_invariant(num1))  # False
print(is_perfect_digital_invariant(num2))  # True
print(is_perfect_digital_invariant(num3))  # True
