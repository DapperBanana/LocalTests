
# Flight reservation system simulation

class Flight:
    def __init__(self, flight_number, destination, capacity, booked_seats=0):
        self.flight_number = flight_number
        self.destination = destination
        self.capacity = capacity
        self.booked_seats = booked_seats

    def available_seats(self):
        return self.capacity - self.booked_seats

    def book_seat(self, num_seats):
        if self.available_seats() >= num_seats:
            self.booked_seats += num_seats
            print(f"Successfully booked {num_seats} seat(s) for flight {self.flight_number} to {self.destination}.")
        else:
            print("Not enough seats available on this flight.")

# Sample flights
flight1 = Flight("F001", "New York", 200)
flight2 = Flight("F002", "Los Angeles", 150)

# User interface
while True:
    print("\nFlight Reservation System")
    print("1. Book a seat")
    print("2. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        flight_choice = input("Enter flight number (F001 for New York, F002 for Los Angeles): ")
        num_seats = int(input("Enter number of seats to book: "))

        if flight_choice == "F001":
            flight1.book_seat(num_seats)
        elif flight_choice == "F002":
            flight2.book_seat(num_seats)
        else:
            print("Invalid flight number.")

    elif choice == "2":
        print("Thank you for using the Flight Reservation System. Have a great flight!")
        break

    else:
        print("Invalid choice. Please try again.")
