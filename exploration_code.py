
def print_calendar(year, month):
    import calendar
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    print(f"{'='*20}")
    print(f"{month_name} {year}")
    print(f"{'='*20}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    for week in cal:
        for day in week:
            if day == 0:
                print("    ", end='')
            else:
                print(f"{day:2}  ", end='')
        print()

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print_calendar(year, month)
