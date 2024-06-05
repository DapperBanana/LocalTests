
def to_title_case(input_string):
    words = input_string.split()
    title_case_words = [word.capitalize() for word in words]
    return ' '.join(title_case_words)

input_string = input("Enter a string: ")
title_case_string = to_title_case(input_string)
print("String in title case: ", title_case_string)
