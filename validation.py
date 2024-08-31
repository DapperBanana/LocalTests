
# Function to calculate GCD
def calculate_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# Function to calculate LCM
def calculate_lcm(x, y):
    gcd = calculate_gcd(x, y)
    lcm = (x*y) // gcd
    return lcm

# Input the numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate and display the LCM
print(f"The LCM of {num1} and {num2} is: {calculate_lcm(num1, num2)}")
