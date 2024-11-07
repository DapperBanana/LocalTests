
def square_root(num):
    return num ** 0.5

num = float(input("Enter a number: "))

if num < 0:
    print("Square root is not real for negative numbers")
else:
    result = square_root(num)
    print(f"The square root of {num} is {result}")
