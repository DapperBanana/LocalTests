
def is_palindrome(year):
    year_str = str(year)
    return year_str == year_str[::-1]

year = int(input("Enter a year: "))

if is_palindrome(year):
    print(year, "is a palindrome year.")
else:
    print(year, "is not a palindrome year.")
