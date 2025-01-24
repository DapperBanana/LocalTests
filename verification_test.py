
def reverse_string(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string to reverse: ")
    reversed_string = reverse_string(user_input)
    print(f"The reversed string is: {reversed_string}")
