
def title_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# Test the function
input_string = "hello world"
output_string = title_case(input_string)
print(output_string)  # Output: Hello World
