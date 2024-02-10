
def is_perfect_digital_invariant(num):
    squared_num = num ** 2
    concatenated_num = str(num) + str(squared_num)
    if int(concatenated_num) == num:
        return True
    else:
        return False

# Testing the function
num = int(input("Enter a number: "))
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")
