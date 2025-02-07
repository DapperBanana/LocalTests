
def sum_of_natural_numbers(n):
    if n < 0:
        return "Please enter a positive integer."

    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

n = int(input("Enter a positive integer n: "))
result = sum_of_natural_numbers(n)

print(f"The sum of the first {n} natural numbers is: {result}")
