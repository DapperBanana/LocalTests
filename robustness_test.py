
def is_palindrome_year(year):
    year_str = str(year)
    reversed_year_str = year_str[::-1]
    return year_str == reversed_year_str

year = int(input("Enter a year to check if it is a palindrome year: "))
if is_palindrome_year(year):
    print(f"{year} is a palindrome year.")
else:
    print(f"{year} is not a palindrome year.")
