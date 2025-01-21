
def is_palindrome_year(year):
    # Convert the year to a string
    year_str = str(year)
    
    # Check if the year is a palindrome by comparing the string with its reverse
    if year_str == year_str[::-1]:
        return True
    else:
        return False

year = int(input("Enter a year to check if it is a palindrome year: "))

if is_palindrome_year(year):
    print(f"{year} is a palindrome year.")
else:
    print(f"{year} is not a palindrome year.")
