
def even_fib_sum(limit):
    # Initialize variables
    fib_num_1 = 1
    fib_num_2 = 2
    even_fib_sum = 0

    # Iterate until the Fibonacci number exceeds the limit
    while fib_num_2 <= limit:
        # Check if the Fibonacci number is even
        if fib_num_2 % 2 == 0:
            even_fib_sum += fib_num_2

        # Generate the next Fibonacci number
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2

    return even_fib_sum

# Test the function
limit = int(input("Enter the limit: "))
result = even_fib_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)
