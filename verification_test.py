
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("\nFlight Reservation System")
        print("1. Book a flight")
        print("2. View booked flights")
        print("3. Cancel a booking")
        print("4. Exit")

    def book_flight(self):
        name = input("Enter passenger name: ")
        flight_number = input("Enter flight number: ")
        seat_number = input("Enter seat number: ")
        self.passenger_list.append({"name": name, "flight_number": flight_number, "seat_number": seat_number})
        print("Flight booked successfully!")

    def view_booked_flights(self):
        for passenger in self.passenger_list:
            print(f"Name: {passenger['name']}, Flight Number: {passenger['flight_number']}, Seat Number: {passenger['seat_number']}")

    def cancel_booking(self):
        name = input("Enter passenger name: ")
        flight_number = input("Enter flight number: ")
        seat_number = input("Enter seat number: ")
        for passenger in self.passenger_list:
            if passenger['name'] == name and passenger['flight_number'] == flight_number and passenger['seat_number'] == seat_number:
                self.passenger_list.remove(passenger)
                print("Booking cancelled successfully!")
                return
        print("No booking found for given details.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.book_flight()
            elif choice == '2':
                self.view_booked_flights()
            elif choice == '3':
                self.cancel_booking()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    flight_system = FlightReservationSystem()
    flight_system.run()
