
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")

    distance = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            distance += 1

    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between 'karolin' and 'kathrin' is:", hamming_distance(str1, str2))

str1 = "1011101"
str2 = "1001001"
print("Hamming distance between '1011101' and '1001001' is:", hamming_distance(str1, str2))

