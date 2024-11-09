
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci sequence is: {result}")
