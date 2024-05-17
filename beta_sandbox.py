
def even_fibonacci_sum(limit):
    a = 1
    b = 1
    total = 0
    
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
        
    return total

limit = int(input("Enter the limit for Fibonacci numbers: "))
sum = even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to {} is: {}".format(limit, sum))
