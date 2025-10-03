
def sum_of_digits(n):
    # Convert the number to a string to iterate through each digit
    str_n = str(n)
    
    # Initialize a variable to store the sum of digits
    sum_digits = 0
    
    # Iterate through each digit in the number and add it to the sum_digits variable
    for digit in str_n:
        sum_digits += int(digit)
    
    return sum_digits

# Input a number from user
num = int(input("Enter a number: "))

# Calculate the sum of digits in the given number
result = sum_of_digits(num)

print("The sum of digits in the number is:", result)
