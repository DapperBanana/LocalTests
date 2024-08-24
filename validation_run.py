
class Flight:
    def __init__(self, number, destination, capacity, booked):
        self.number = number
        self.destination = destination
        self.capacity = capacity
        self.booked = booked

    def checkAvailability(self):
        return self.capacity - self.booked

flights = [
    Flight(101, "New York", 150, 75),
    Flight(202, "Los Angeles", 200, 100),
    Flight(303, "Chicago", 180, 50)
]

def displayFlights():
    print("Available Flights:")
    for flight in flights:
        print(f"Flight Number: {flight.number}, Destination: {flight.destination}, Seats Available: {flight.checkAvailability()}")

def bookFlight(flight_num, num_passengers):
    for flight in flights:
        if flight.number == flight_num:
            available_seats = flight.checkAvailability()
            if available_seats >= num_passengers:
                flight.booked += num_passengers
                print(f"Flight {flight_num} booked successfully for {num_passengers} passengers!")
                return
            else:
                print(f"Not enough seats available on flight {flight_num}. Available seats: {available_seats}")
                return
    print(f"Flight with number {flight_num} not found.")

def main():
    while True:
        print("\n1. Display available flights")
        print("2. Book a flight")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            displayFlights()
        elif choice == '2':
            flight_num = int(input("Enter flight number: "))
            num_passengers = int(input("Enter number of passengers: "))
            bookFlight(flight_num, num_passengers)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
