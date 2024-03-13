
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of equal length")
    
    distance = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            distance += 1
    
    return distance

# Test the function
string1 = "karolin"
string2 = "kathrin"
print(f"The Hamming distance between '{string1}' and '{string2}' is {hamming_distance(string1, string2)}")

string3 = "1011101"
string4 = "1001001"
print(f"The Hamming distance between '{string3}' and '{string4}' is {hamming_distance(string3, string4)}")
