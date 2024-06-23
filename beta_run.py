
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Get input from user
input_string = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(input_string)

# Display the reversed string
print(f"The reversed string is: {reversed_string}")
