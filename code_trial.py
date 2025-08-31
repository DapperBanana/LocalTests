
import calendar

def print_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    
    print(calendar.month_name[month], year)
    print('Mo Tu We Th Fr Sa Su')
    
    for week in cal:
        for day in week:
            if day == 0:
                print('   ', end=' ')
            else:
                print(f'{day:2}', end=' ')
        print()

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    print_calendar(year, month)

if __name__ == '__main__':
    main()
