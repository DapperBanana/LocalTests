
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # convert string to lower case and remove spaces
    return s == s[::-1]  # check if string is equal to its reverse

# Test the function
if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_palindrome(string):
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
