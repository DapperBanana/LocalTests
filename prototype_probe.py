
def convert_to_titlecase(text):
    return ' '.join(word.capitalize() for word in text.split())

input_text = input("Enter a string: ")
titlecased_text = convert_to_titlecase(input_text)
print("Title cased string: ", titlecased_text)
