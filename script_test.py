
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

# Get input from user
input_string = input("Enter a string: ")

# Call the function to reverse the input string
reversed_string = reverse_string(input_string)

# Output the reversed string
print("Reversed string:", reversed_string)
