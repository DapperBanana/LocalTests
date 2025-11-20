
def is_perfect_square(num):
    if num < 0:
        return False

    root = int(num ** 0.5)
    return root * root == num

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
