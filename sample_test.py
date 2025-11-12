
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    
    if n < 0:
        print("Please enter a positive integer.")
    else:
        result = sum_of_natural_numbers(n)
        print(f"The sum of the first {n} natural numbers is: {result}")
