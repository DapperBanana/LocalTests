
def longest_common_prefix(strs):
    # Handle the case when the list is empty
    if len(strs) == 0:
        return ""

    # Sort the strings in alphabetical order
    strs.sort()

    # Find the common prefix between the first and last string
    common_prefix = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            common_prefix += strs[0][i]
        else:
            break

    return common_prefix

# Test the function
strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))
# Output: "fl"

strings = ["dog", "racecar", "car"]
print(longest_common_prefix(strings))
# Output: ""
