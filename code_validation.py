
def is_palindrome_year(year):
    year_str = str(year)
    return year_str == year_str[::-1]

year = input("Enter a year: ")

if year.isdigit():
    year = int(year)
    if is_palindrome_year(year):
        print(f"{year} is a palindrome year.")
    else:
        print(f"{year} is not a palindrome year.")
else:
    print("Please enter a valid year.")
