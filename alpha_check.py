
def print_calendar(year, month):
    import calendar
    
    cal = calendar.month(year, month)
    print(cal)

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    
    print_calendar(year, month)

if __name__ == "__main__":
    main()
