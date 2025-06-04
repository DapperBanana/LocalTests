
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

n = int(input("Enter the value of n: "))
print(f"The {n}th term of the Fibonacci sequence is {fibonacci(n)}")
