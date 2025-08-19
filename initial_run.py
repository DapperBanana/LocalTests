
def factorial(num):
    if num < 0:
        return "Factorial is undefined for negative numbers"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
