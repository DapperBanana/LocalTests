
def roman_to_integer(s):
    # Create a dictionary to map the Roman numerals to their respective values
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the result and a variable to keep track of the previous numeral's value
    result = 0
    previous_value = 0
    
    # Iterate backward through the Roman numeral string
    for i in range(len(s) - 1, -1, -1):
        current_value = roman_values[s[i]]
        
        # If the current numeral is smaller than the previous one, subtract its value
        if current_value < previous_value:
            result -= current_value
        # Otherwise, add its value to the result
        else:
            result += current_value
            
        # Update the previous numeral's value for the next iteration
        previous_value = current_value
    
    return result

# Test the function
numeral = input("Enter a Roman numeral: ")
print("Integer value:", roman_to_integer(numeral))
