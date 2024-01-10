
def digit_sum(num):
    # Keep calculating sum until num becomes a single-digit number
    while num > 9:
        total_sum = 0
        
        # Calculate the sum of the digits
        while num > 0:
            total_sum += num % 10
            num //= 10
        
        # Update the num with the new sum
        num = total_sum
    
    return num


# Test the program
number = int(input("Enter a number: "))
sum_of_digits = digit_sum(number)
print("Sum of digits until it becomes a single-digit number:", sum_of_digits)
