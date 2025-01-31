
def print_calendar(month, year):
    import calendar
    cal = calendar.monthcalendar(year, month)
    weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

    print("{:^20}".format(calendar.month_name[month]))
    print(" ".join(weeks))

    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=' ')
            else:
                print("{:2}".format(day), end=' ')
        print()

while True:
    print("\nWelcome to the Text-based Calendar!")
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    if month < 1 or month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
        continue

    print_calendar(month, year)

    choice = input("\nWould you like to view another month? (y/n): ")
    if choice.lower() != 'y':
        print("Thank you for using the Text-based Calendar. Goodbye!")
        break
