
def display_calendar(year, month):
    import calendar
    
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    headers = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    print(f"{month_name} {year}")
    print(' '.join(headers))
    
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2} "
        print(week_str)
        

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    display_calendar(year, month)
