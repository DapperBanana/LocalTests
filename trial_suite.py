
def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a positive integer n: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = calculate_sum(n)
    print(f"The sum of the first {n} natural numbers is: {result}")
