
def display_calendar(month, year):
    import calendar

    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    year_str = str(year)

    print(f"   {month_name} {year_str}")
    print("Mo Tu We Th Fr Sa Su")

    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2} "
        print(week_str)

if __name__ == "__main__":
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))

    display_calendar(month, year)
