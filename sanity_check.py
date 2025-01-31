
def is_perfect_digital_invariant(num):
    num_str = str(num)
    for i in range(len(num_str)):
        if int(num_str[i]) != num % 10:
            return False
        num = num // 10
    return True

num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
