
class Flight:
    def __init__(self, flight_number, departure, destination, seats, price):
        self.flight_number = flight_number
        self.departure = departure
        self.destination = destination
        self.seats = seats
        self.price = price

flights = [
    Flight("F1001", "New York", "Los Angeles", 100, 200),
    Flight("F1002", "Chicago", "Miami", 150, 250),
    Flight("F1003", "Seattle", "Houston", 120, 220),
    Flight("F1004", "Boston", "San Francisco", 90, 180),
]

def display_flights():
    for flight in flights:
        print(f"Flight Number: {flight.flight_number}")
        print(f"Departure: {flight.departure}")
        print(f"Destination: {flight.destination}")
        print(f"Available Seats: {flight.seats}")
        print(f"Price: ${flight.price}")
        print("--------------------------")

def reserve_flight(flight_number, num_seats):
    for flight in flights:
        if flight.flight_number == flight_number:
            if flight.seats >= num_seats:
                flight.seats -= num_seats
                total_price = flight.price * num_seats
                print(f"{num_seats} seats reserved for Flight {flight_number}. Total Price: ${total_price}")
            else:
                print("Not enough seats available for this flight.")
            return
    print("Flight not found.")

def main():
    while True:
        print("Welcome to the Flight Reservation System")
        print("1. Display Available Flights")
        print("2. Reserve a Flight")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_flights()
        elif choice == "2":
            flight_number = input("Enter the flight number: ")
            num_seats = int(input("Enter the number of seats to reserve: "))
            reserve_flight(flight_number, num_seats)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
