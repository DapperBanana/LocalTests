
def print_calendar(year, month):
    import calendar

    cal = calendar.monthcalendar(year, month)
    header = calendar.month_name[month] + " " + str(year)
    days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    print(header.center(20))
    print(' '.join(days))
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '   '
            else:
                week_str += str(day).rjust(2) + ' '
        print(week_str)

# Get user input for year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

print_calendar(year, month)
