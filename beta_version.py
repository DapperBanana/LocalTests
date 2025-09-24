
def display_calendar(year, month):
    import calendar
    
    cal = calendar.monthcalendar(year, month)
    
    print("       {0} {1}".format(calendar.month_name[month], year))
    print("Mo Tu We Th Fr Sa Su")
    
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end="")
            else:
                print("{:2} ".format(day), end="")
        print()

# Get user input for year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Display the calendar
display_calendar(year, month)
