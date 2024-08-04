
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("1. Show available flights")
        print("2. Reserve a flight")
        print("3. Cancel a reservation")
        print("4. Show passenger list")
        print("5. Exit")

    def show_available_flights(self):
        print("Available flights:")
        print("1. Flight 101 - New York to Los Angeles")
        print("2. Flight 202 - Chicago to Miami")
        print("3. Flight 303 - San Francisco to Seattle")

    def reserve_flight(self, passenger_name, flight_number):
        self.passenger_list.append((passenger_name, flight_number))
        print("Reservation successful!")

    def cancel_reservation(self, passenger_name, flight_number):
        for passenger in self.passenger_list:
            if passenger[0] == passenger_name and passenger[1] == flight_number:
                self.passenger_list.remove(passenger)
                print("Reservation cancelled.")
                return
        print("Passenger or flight not found.")

    def show_passenger_list(self):
        print("Passenger List:")
        for passenger in self.passenger_list:
            print(f"{passenger[0]} - Flight {passenger[1]}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_available_flights()
            elif choice == "2":
                passenger_name = input("Enter passenger name: ")
                flight_number = input("Enter flight number: ")
                self.reserve_flight(passenger_name, flight_number)
            elif choice == "3":
                passenger_name = input("Enter passenger name: ")
                flight_number = input("Enter flight number: ")
                self.cancel_reservation(passenger_name, flight_number)
            elif choice == "4":
                self.show_passenger_list()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    flight_reservation_system = FlightReservationSystem()
    flight_reservation_system.run()
