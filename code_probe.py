
class Flight:
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, arrival_time, capacity, booked_seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity = capacity
        self.booked_seats = booked_seats

    def check_availability(self):
        return self.capacity - self.booked_seats

    def book_seat(self, num_seats):
        if self.check_availability() >= num_seats:
            self.booked_seats += num_seats
            print(f"{num_seats} seat(s) booked successfully for Flight {self.flight_number}.")
        else:
            print("Not enough seats available on this flight.")

flights = [
    Flight("AA123", "New York", "Los Angeles", "10:00", "13:00", 150, 50),
    Flight("BA456", "London", "Paris", "12:00", "15:00", 100, 20),
    Flight("CX789", "Hong Kong", "Tokyo", "14:00", "17:00", 200, 100)
]

def display_flights():
    for flight in flights:
        print(f"Flight Number: {flight.flight_number}")
        print(f"From: {flight.departure_city} - To: {flight.arrival_city}")
        print(f"Departure Time: {flight.departure_time} - Arrival Time: {flight.arrival_time}")
        print(f"Seats Available: {flight.check_availability()}\n")

print("Welcome to the Flight Reservation System!")
while True:
    print("Choose an option:")
    print("1. Display available flights")
    print("2. Book a seat")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_flights()
    elif choice == "2":
        display_flights()
        flight_number = input("Enter the flight number you want to book a seat for: ")
        num_seats = int(input("Enter the number of seats you want to book: "))
        for flight in flights:
            if flight.flight_number == flight_number:
                flight.book_seat(num_seats)
                break
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Flight Reservation System. Have a nice day!")
