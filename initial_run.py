
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == "__main__":
    lst = [1, 2, 3, 2, 1, 4, 5, 6, 4]
    result = remove_duplicates(lst)
    print(result)
