
def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Example usage        
my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average of the numbers in the list is: {average}")
