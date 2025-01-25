
def print_calendar(month, year):
    import calendar

    cal = calendar.monthcalendar(year, month)
    header = calendar.month_name[month] + ' ' + str(year)
    days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    print(header.center(20))
    print(' '.join(days_of_week))
    
    for week in cal:
        for day in week:
            if day == 0:
                print('   ', end=' ')
            else:
                print(str(day).rjust(2), end=' ')
        print()
              
print_calendar(9, 2023)
