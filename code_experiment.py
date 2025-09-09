
def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

n = int(input("Enter a value for n: "))
result = sum_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
