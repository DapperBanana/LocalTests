
def display_calendar(month, year):
    import calendar
    cal = calendar.monthcalendar(year, month)
    
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    print('{:^20}'.format(calendar.month_abbr[month]), year)
    
    print(' '.join(weekdays))
    
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '    '
            else:
                week_str += '{:>3}'.format(day)
        print(week_str)

while True:
    user_input = input("Enter a month and year (MM YYYY) or enter 'q' to quit: ")

    if user_input.lower() == 'q':
        break
    
    try:
        month, year = map(int, user_input.split())
        if month < 1 or month > 12 or year < 1900:  # Basic validation for month and year
            print("Invalid input. Please enter a valid month and year")
        else:
            display_calendar(month, year)
    except ValueError:
        print("Invalid input. Please enter a valid month and year")
