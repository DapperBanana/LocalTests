
def even_fibonacci_sum(limit):
    # Initialize variables to store the current and previous Fibonacci numbers
    f1, f2 = 1, 1
    # Initialize variable to store the sum of even Fibonacci numbers
    even_sum = 0

    # Loop through Fibonacci numbers up to the limit
    while f2 <= limit:
        # Check if the current Fibonacci number is even
        if f2 % 2 == 0:
            even_sum += f2

        # Calculate the next Fibonacci number
        f1, f2 = f2, f1 + f2

    return even_sum

# Get the upper limit from the user
limit = int(input("Enter the limit: "))

# Calculate the sum of even Fibonacci numbers up to the given limit
result = even_fibonacci_sum(limit)
print("Sum of even Fibonacci numbers up to", limit, "is:", result)
