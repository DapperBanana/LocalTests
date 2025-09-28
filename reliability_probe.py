
def sum_of_digits(number):
    # Check if number is a single-digit number
    while number > 9:
        temp = number
        total = 0
        
        # Calculate sum of digits
        while temp > 0:
            total += temp % 10
            temp = temp // 10
        
        number = total
    
    return number

# Input number from user
num = int(input("Enter a number: "))

# Calculate sum of digits until it becomes a single-digit number
result = sum_of_digits(num)
print("Sum of digits of the number until it becomes a single-digit number:", result)
