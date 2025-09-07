
def sum_of_natural_numbers(n):
    if n < 0:
        return "Please enter a positive integer"
    else:
        sum = 0
        for i in range(1, n+1):
            sum += i
        return sum

# Input the value of n
n = int(input("Enter the value of n: "))

# Calculate and display the sum of the first n natural numbers
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
