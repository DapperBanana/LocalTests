
def calculate_sum(n):
    return n * (n + 1) // 2

n = int(input("Enter a positive integer n: "))
result = calculate_sum(n)

print(f"The sum of the first {n} natural numbers is: {result}")
