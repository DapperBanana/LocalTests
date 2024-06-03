
def count_words(input_string):
    words = input_string.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

input_string = "hello world hello python python python"
print(count_words(input_string))
