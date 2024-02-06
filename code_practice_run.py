
def calculate_average(numbers):
    sum_of_numbers = sum(numbers)
    average = sum_of_numbers / len(numbers)
    return average

# sample list
numbers = [2, 4, 6, 8, 10]

# calculate the average and print it
average = calculate_average(numbers)
print("The average is:", average)
