
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
result = is_even_or_odd(num)
print(f"The number {num} is {result}.")
