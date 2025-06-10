
def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

# Get input from user
input_str = input("Enter a string: ")

# Call the function to reverse the string
reversed_str = reverse_string(input_str)

# Print the reversed string
print("Reversed string:", reversed_str)
