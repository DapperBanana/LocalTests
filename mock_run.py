
def reverse_string(s):
    reversed_string = ""
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string

# Test the function
input_string = "hello world"
reversed_output = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_output)
