
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

def calculator():
    operation = input("Enter an operation (+, -, *, /): ")
    
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation")
        return
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    else:
        result = divide(num1, num2)
        
    print("Result: ", result)

calculator()
