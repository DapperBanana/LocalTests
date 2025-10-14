
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("Welcome to the Flight Reservation System!")
        print("1. Add Passenger")
        print("2. Display Passengers")
        print("3. Exit")

    def add_passenger(self):
        name = input("Enter passenger name: ")
        seat_number = input("Enter seat number: ")
        self.passenger_list.append({"name": name, "seat_number": seat_number})
        print("Passenger added successfully!")

    def display_passengers(self):
        if len(self.passenger_list) == 0:
            print("No passengers added yet.")
        else:
            print("Passengers:")
            for passenger in self.passenger_list:
                print("Name: " + passenger["name"] + ", Seat Number: " + passenger["seat_number"])

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_passenger()
            elif choice == "2":
                self.display_passengers()
            elif choice == "3":
                print("Exiting program. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    reservation_system = FlightReservationSystem()
    reservation_system.run()
