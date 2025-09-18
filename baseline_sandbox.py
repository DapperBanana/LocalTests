
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be of the same length")
    
    distance = 0
    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            distance += 1

    return distance

# Test the function with example strings
string1 = "karolin"
string2 = "kathrin"
print(f"The Hamming distance between '{string1}' and '{string2}' is: {hamming_distance(string1, string2)}")
