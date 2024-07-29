
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("\nWelcome to the Flight Reservation System")
        print("1. Reserve a seat")
        print("2. View passenger list")
        print("3. Exit")

    def reserve_seat(self):
        name = input("Enter passenger name: ")
        seat = input("Enter seat number: ")

        self.passenger_list.append((name, seat))
        print("Seat reserved for", name)

    def view_passenger_list(self):
        if not self.passenger_list:
            print("No passengers have reserved seats yet.")
        else:
            print("Passenger List:")
            for i, passenger in enumerate(self.passenger_list, 1):
                print(f"{i}. {passenger[0]} - Seat {passenger[1]}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.reserve_seat()
            elif choice == '2':
                self.view_passenger_list()
            elif choice == '3':
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = FlightReservationSystem()
    system.run()
