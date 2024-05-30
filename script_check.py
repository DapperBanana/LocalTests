
def is_leap_year(year):
    if year % 4 == 0:  # Leap year is divisible by 4
        if year % 100 == 0:  # Unless it is divisible by 100
            if year % 400 == 0:  # If divisible by 400, it is a leap year
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
