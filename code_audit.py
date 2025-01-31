
def longest_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = ""
    for i in range(len(min(strings, key=len))):
        if all(s[i] == strings[0][i] for s in strings):
            prefix += strings[0][i]
        else:
            break
    
    return prefix

# Test the function
strings = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strings))

strings = ["dog", "racecar", "car"]
print("Longest common prefix:", longest_common_prefix(strings))

strings = ["apple", "banana", "cherry"]
print("Longest common prefix:", longest_common_prefix(strings))
