
def print_calendar(year, month):
    import calendar
    cal = calendar.monthcalendar(year, month)
    print(calendar.month_name[month], year)
    print('Mo Tu We Th Fr Sa Su')
    for week in cal:
        for day in week:
            if day == 0:
                print('   ', end='')
            else:
                print(f'{day:2} ', end='')
        print()

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print_calendar(year, month)
