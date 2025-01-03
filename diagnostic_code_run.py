
def is_perfect_digital_invariant(num):
    num_str = str(num)
    
    if len(num_str) == 1:
        return True
    
    for i in range(1, len(num_str)):
        if int(num_str[i]) - int(num_str[i-1]) != 1:
            return False
    
    return True

num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
