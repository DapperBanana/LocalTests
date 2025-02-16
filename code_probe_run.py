
def print_calendar(year, month):
    import calendar
    
    # Create a calendar object
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Print the calendar for the given year and month
    print(cal.formatmonth(year, month))

# Get user input for the year and month
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Display the calendar
print_calendar(year, month)
