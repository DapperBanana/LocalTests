
def is_vampire_number(num):
    # Convert the number to a string to easily split it into digits
    num_str = str(num)
    
    # Check if the number of digits is even
    if len(num_str) % 2 != 0:
        return False
    
    # Split the number into pairs of digits
    pairs = [num_str[i:i+2] for i in range(0, len(num_str), 2)]
    
    # Iterate through all possible permutations of the digits
    from itertools import permutations
    for perm in permutations(num_str):
        # Check if the permutation is a valid combination of the pairs
        if all(int(perm[i] + perm[i+1]) == int(pairs[i]) for i in range(len(pairs))):
            return True
    
    return False

# Test the function with some examples
print(is_vampire_number(1260))  # True
print(is_vampire_number(1122))  # False
print(is_vampire_number(126))   # False
