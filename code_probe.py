
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print("Welcome to the Basic Calculator")

while True:
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result: ", add(num1, num2))
        elif choice == '2':
            print("Result: ", subtract(num1, num2))
        elif choice == '3':
            print("Result: ", multiply(num1, num2))
        elif choice == '4':
            print("Result: ", divide(num1, num2))
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
