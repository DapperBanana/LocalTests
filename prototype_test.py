
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Test the function
string1 = "karolin"
string2 = "kathrin"
print("Hamming distance between '{}' and '{}' is: {}".format(string1, string2, hamming_distance(string1, string2)))

string3 = "1011101"
string4 = "1001001"
print("Hamming distance between '{}' and '{}' is: {}".format(string3, string4, hamming_distance(string3, string4)))
