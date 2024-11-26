
class Flight:
    def __init__(self, flight_number, destination, departure_time, arrival_time, price, seats_available):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats_available = seats_available

flights = [Flight("AA123", "New York", "10:00", "12:00", 200, 100),
           Flight("BB456", "Los Angeles", "12:30", "14:30", 250, 50),
           Flight("CC789", "Chicago", "15:00", "17:00", 180, 75)]

def display_flights():
    print("Available Flights:")
    for flight in flights:
        print(f"Flight Number: {flight.flight_number}, Destination: {flight.destination}, Departure Time: {flight.departure_time}, Arrival Time: {flight.arrival_time}, Price: ${flight.price}, Seats Available: {flight.seats_available}")
    print()

def make_reservation():
    flight_number = input("Enter the flight number you want to book: ")
    for flight in flights:
        if flight.flight_number == flight_number:
            if flight.seats_available > 0:
                flight.seats_available -= 1
                print("Reservation successful! Enjoy your flight.")
            else:
                print("Sorry, this flight is fully booked.")
            return
    print("Invalid flight number.")

while True:
    print("Welcome to the Flight Reservation System")
    print("1. Display Available Flights")
    print("2. Make a Reservation")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_flights()
    elif choice == "2":
        make_reservation()
    elif choice == "3":
        print("Thank you for using the Flight Reservation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    print()
