
def convert_to_title_case(string):
    words = string.split()
    title_case_words = [word.capitalize() for word in words]
    return ' '.join(title_case_words)

input_string = input("Enter a string: ")
title_case_string = convert_to_title_case(input_string)
print("Title Case String:", title_case_string)
