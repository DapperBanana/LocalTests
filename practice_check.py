
def print_calendar(year, month):
    import calendar
    cal = calendar.monthcalendar(year, month)
    header = calendar.month_name[month] + ' ' + str(year)
    
    print('{:^20}'.format(header))
    print('Mo Tu We Th Fr Sa Su')

    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '   '
            else:
                week_str += '{:2} '.format(day)
        print(week_str)

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print_calendar(year, month)
