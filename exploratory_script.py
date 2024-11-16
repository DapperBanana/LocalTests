
def sort_list(nums):
    nums.sort()
    return nums

# taking input from user
numbers = input("Enter a list of numbers separated by space: ")
nums = [int(i) for i in numbers.split()]

sorted_nums = sort_list(nums)
print("Numbers in ascending order:", sorted_nums)
