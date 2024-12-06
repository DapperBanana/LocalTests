
# basic text-based calendar program

def print_calendar(month, year):
    import calendar
    cal = calendar.monthcalendar(year, month)
    
    # print month and year
    print(calendar.month_name[month], year)
    
    # print weekdays
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print(" ".join(weekdays))
    
    # print calendar days
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   " # add space if day is zero
            else:
                week_str += f"{day:2d} " # format day to have 2 digits
        print(week_str)

# input month and year from user
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

print_calendar(month, year)
