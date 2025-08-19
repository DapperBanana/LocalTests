
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("Flight Reservation System")
        print("1. Reserve a seat")
        print("2. View passenger list")
        print("3. Exit")

    def reserve_seat(self):
        name = input("Enter passenger name: ")
        seat_number = input("Enter seat number: ")
        self.passenger_list.append({"name": name, "seat_number": seat_number})
        print("Seat reserved successfully!")

    def view_passenger_list(self):
        print("Passenger list:")
        for passenger in self.passenger_list:
            print(f"Name: {passenger['name']}, Seat number: {passenger['seat_number']}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.reserve_seat()
            elif choice == '2':
                self.view_passenger_list()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


system = FlightReservationSystem()
system.run()
