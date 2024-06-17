
def is_palindrome_year(year):
    # Convert year to a string for easy comparison
    year_str = str(year)
    
    # Check if the year is a palindrome
    if year_str == year_str[::-1]:
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_palindrome_year(year):
    print(f"{year} is a palindrome year!")
else:
    print(f"{year} is not a palindrome year.")
