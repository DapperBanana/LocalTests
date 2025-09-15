
def hamming_distance(str1, str2):
    distance = 0
    if len(str1) != len(str2):
        raise ValueError("String lengths are not equal")
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

str1 = "karolin"
str2 = "kathrin"
print("Hamming distance between '{}' and '{}' is: {}".format(str1, str2, hamming_distance(str1, str2)))
