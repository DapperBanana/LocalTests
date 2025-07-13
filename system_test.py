
def fibonacci_sequence(n):
    # initialize first two terms
    a, b = 0, 1
    count = 0

    # check if number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence up to", n, "terms:")
        print(a)
    else:
        print("Fibonacci sequence up to", n, "terms:")
        while count < n:
            print(a, end=" ")
            nth = a + b
            # update values for next iteration
            a = b
            b = nth
            count += 1

# get user input for number of terms
n = int(input("Enter the number of terms for Fibonacci sequence: "))
fibonacci_sequence(n)
