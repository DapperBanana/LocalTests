
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("-------- Basic Calculator --------")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

if operation == '+':
    result = add(num1, num2)
    print("Result: ", result)
elif operation == '-':
    result = subtract(num1, num2)
    print("Result: ", result)
elif operation == '*':
    result = multiply(num1, num2)
    print("Result: ", result)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = divide(num1, num2)
        print("Result: ", result)
else:
    print("Invalid operation")
