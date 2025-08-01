
def print_calendar(month, year):
    import calendar
    cal = calendar.monthcalendar(year, month)
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    print("\n" + months[month-1] + " " + str(year))
    print("Mo Tu We Th Fr Sa Su")
    
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += "{:2d} ".format(day)
        print(week_str)

while True:
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    
    if month < 1 or month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
    else:
        print_calendar(month, year)
        break
