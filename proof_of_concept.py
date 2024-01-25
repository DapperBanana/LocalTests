
def count_characters(string):
    # Initialize an empty dictionary to store the count of each character
    count = {}

    # Iterate through each character in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char in count:
            # If it is, increment its count by 1
            count[char] += 1
        else:
            # If it is not, add it to the dictionary with a count of 1
            count[char] = 1

    # Print the count of each character
    for char, count in count.items():
        print(f"{char}: {count}")

# Test the function
string = "hello world"
count_characters(string)
