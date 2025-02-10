
def remove_duplicates(input_list):
    no_duplicates = []
    seen = set()

    for value in input_list:
        if value not in seen:
            no_duplicates.append(value)
            seen.add(value)

    return no_duplicates

# Test the function
input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print(result)
