
def longest_common_prefix(strings):
    if not strings:
        return ""

    shortest_string = min(strings, key=len)
    for i, char in enumerate(shortest_string):
        for string in strings:
            if string[i] != char:
                return shortest_string[:i]
    return shortest_string

# Test the function
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # Output: "fl"
