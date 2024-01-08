
import calendar

def get_events():
    events = {}
    while True:
        event = input("Enter event (or 'exit' to quit): ")
        if event.lower() == 'exit':
            break
        date = input("Enter date (MM/DD/YYYY): ")
        events[date] = events.get(date, []) + [event]
    return events

def print_calendar(year, month, events):
    print(calendar.month_name[month], year)
    print(calendar.weekheader(3))
    calendar.setfirstweekday(calendar.SUNDAY)
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end='')
            else:
                if len(str(day)) == 1:
                    day = " " + str(day)
                date = '{:02d}/{:02d}/{:04d}'.format(month, day, year)
                if date in events:
                    print("[{}]".format(day), end='')
                else:
                    print(" {} ".format(day), end='')
        print()

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    events = get_events()
    print_calendar(year, month, events)

if __name__ == '__main__':
    main()
