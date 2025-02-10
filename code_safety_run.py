
def sort_list_ascending(numbers):
    numbers.sort()
    return numbers

if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = sort_list_ascending(numbers)
    print(sorted_numbers)
