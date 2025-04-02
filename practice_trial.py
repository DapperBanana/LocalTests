
def sum_of_natural_numbers(n):
    if n < 0:
        return "Please enter a positive number."
    else:
        return n*(n+1)//2

n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
