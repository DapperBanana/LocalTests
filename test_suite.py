
def count_characters(string):
    # Initialize an empty dictionary to store the counts
    count_dict = {}

    # Iterate through each character in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char in count_dict:
            # If it is, increment the count by 1
            count_dict[char] += 1
        else:
            # If it is not, add the character to the dictionary with a count of 1
            count_dict[char] = 1

    # Return the dictionary with the character counts
    return count_dict

# Test the function
input_string = input("Enter a string: ")
character_counts = count_characters(input_string)
print("Character Counts:")
for char, count in character_counts.items():
    print(char, ":", count)
