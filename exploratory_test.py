
def print_calendar(year, month):
    import calendar
    
    # create a calendar object
    cal = calendar.monthcalendar(year, month)
    
    # print month and year
    print(calendar.month_name[month], year)
    print('Mo Tu We Th Fr Sa Su')
    
    # print calendar
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '   '
            else:
                week_str += '{:2d} '.format(day)
        print(week_str)

# get user input
year = int(input('Enter year: '))
month = int(input('Enter month: '))

# print calendar
print_calendar(year, month)
