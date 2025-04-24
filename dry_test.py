
def print_calendar(month, year):
    import calendar
    
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    print(f"{' ' * 15}{month_name} {year}")
    print("Sun Mon Tue Wed Thu Fri Sat")
    
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "    "
            else:
                week_str += f"{day:3} "
        print(week_str)
        
if __name__ == "__main__":
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            if month < 1 or month > 12:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid month (1-12) and year.")
            
    print_calendar(month, year)
