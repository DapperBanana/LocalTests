
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    memo[n] = result
    return result

n = int(input("Enter the value of n: "))
print(f"The {n}th term of the Fibonacci sequence is: {fibonacci(n)}")
