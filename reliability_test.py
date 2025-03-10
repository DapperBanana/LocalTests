
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return None

    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))

str1 = "1011101"
str2 = "1001001"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))

str1 = "abcdef"
str2 = "ABCDEF"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))
