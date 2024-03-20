
def to_title_case(sentence):
    words = sentence.split()
    title_case_words = [word.capitalize() for word in words]
    return ' '.join(title_case_words)

# Test the function
sentence = "hello world"
title_case_sentence = to_title_case(sentence)
print(title_case_sentence)
