
def calculate_average(lst):
    total = sum(lst)
    avg = total / len(lst)
    return avg

if __name__ == "__main__":
    num_list = [5, 10, 15, 20, 25]
    average = calculate_average(num_list)
    print(f"The average of the elements in the list is: {average}")
