
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must have the same length")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

# Test the function
str1 = "karolin"
str2 = "kathrin"
print(f"The Hamming distance between {str1} and {str2} is {hamming_distance(str1, str2)}")

str1 = "1001111"
str2 = "1010101"
print(f"The Hamming distance between {str1} and {str2} is {hamming_distance(str1, str2)}")
