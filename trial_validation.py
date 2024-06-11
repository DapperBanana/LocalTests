
def count_words(string):
    words = string.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Test the function
string = "this is a test string for testing the count of each word in the string"
result = count_words(string)

for word, count in result.items():
    print(f"{word}: {count}")
