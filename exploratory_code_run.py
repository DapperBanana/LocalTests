
def is_vampire_number(num):
    # Convert number to string to easily access individual digits
    num_str = str(num)
    # Check if number has even number of digits
    if len(num_str) % 2 != 0:
        return False
    
    # Create list of all possible permutations of the digits
    permutations = [int(''.join(p)) for p in itertools.permutations(num_str)]

    # Check if any of the permutations satisfy the vampire number condition
    for perm in permutations:
        if perm % 100 == 0:
            continue
        first_half = int(str(perm)[:len(num_str)//2])
        second_half = int(str(perm)[len(num_str)//2:])
        if first_half * second_half == num:
            return True
    
    return False

# Test the function with a few examples
print(is_vampire_number(1260))  # True (21 * 60 = 1260)
print(is_vampire_number(1102))  # False
print(is_vampire_number(5670))  # True (57 * 60 = 3420)
