
class FlightReservationSystem:
    def __init__(self):
        self.flights = {
            "1": {"flight_number": "FL123", "destination": "New York", "departure_time": "10:00 AM", "seats_available": 100},
            "2": {"flight_number": "FL456", "destination": "Los Angeles", "departure_time": "1:00 PM", "seats_available": 50},
            "3": {"flight_number": "FL789", "destination": "Chicago", "departure_time": "4:00 PM", "seats_available": 75}
        }
        self.reservations = {}

    def display_flights(self):
        print("Available Flights:")
        for flight_num, flight_info in self.flights.items():
            print(f"Flight {flight_num}: {flight_info['flight_number']} to {flight_info['destination']} at {flight_info['departure_time']}. Seats available: {flight_info['seats_available']}")

    def make_reservation(self, flight_num, num_passengers):
        if flight_num not in self.flights:
            print("Invalid flight number. Please try again.")
        else:
            if self.flights[flight_num]["seats_available"] >= num_passengers:
                self.flights[flight_num]["seats_available"] -= num_passengers
                reservation_id = len(self.reservations) + 1
                self.reservations[reservation_id] = {"flight_number": self.flights[flight_num]["flight_number"], "num_passengers": num_passengers}
                print(f"Reservation successful. Your reservation ID is: {reservation_id}")
            else:
                print("Not enough seats available on this flight. Please try again.")

    def cancel_reservation(self, reservation_id):
        if reservation_id in self.reservations:
            flight_num = self.reservations[reservation_id]["flight_number"]
            num_passengers = self.reservations[reservation_id]["num_passengers"]
            self.flights[flight_num]["seats_available"] += num_passengers
            del self.reservations[reservation_id]
            print("Reservation cancelled successfully.")
        else:
            print("Invalid reservation ID. Please try again.")

    def display_reservations(self):
        print("Your Reservations:")
        for reservation_id, reservation_info in self.reservations.items():
            print(f"Reservation ID: {reservation_id}, Flight: {reservation_info['flight_number']}, Passengers: {reservation_info['num_passengers']}")

# Main program
reservation_system = FlightReservationSystem()

while True:
    print("\nMenu:")
    print("1. Display available flights")
    print("2. Make a reservation")
    print("3. Cancel a reservation")
    print("4. Display your reservations")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        reservation_system.display_flights()
    elif choice == "2":
        flight_num = input("Enter the flight number you want to reserve: ")
        num_passengers = int(input("Enter the number of passengers: "))
        reservation_system.make_reservation(flight_num, num_passengers)
    elif choice == "3":
        reservation_id = int(input("Enter your reservation ID: "))
        reservation_system.cancel_reservation(reservation_id)
    elif choice == "4":
        reservation_system.display_reservations()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
