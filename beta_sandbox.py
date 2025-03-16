
def print_calendar(year, month):
    import calendar
    cal = calendar.monthcalendar(year, month)
    
    print(f"{'-'*20}")
    print(calendar.month_name[month], year)
    print(f"{'-'*20}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    
    for week in cal:
        week_str = ''
        for day in week:
            if day == 0:
                week_str += '    '
            else:
                week_str += f"{day:3} "
        print(week_str)
        
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print_calendar(year, month)
