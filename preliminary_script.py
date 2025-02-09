
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")

    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))

str1 = "karolin"
str2 = "karolin"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))
