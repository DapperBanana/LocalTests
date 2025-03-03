
def is_perfect_square(num):
    sqrt = num ** 0.5
    return sqrt.is_integer()

num = int(input("Enter a number to check if it is a perfect square: "))

if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
