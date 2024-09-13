
class FlightReservationSystem:
    def __init__(self):
        self.passengers = {}

    def display_menu(self):
        print("1. Reserve a seat")
        print("2. Cancel reservation")
        print("3. Display passengers")
        print("4. Exit")

    def reserve_seat(self):
        name = input("Enter passenger name: ")
        seat_number = input("Enter seat number: ")

        if seat_number in self.passengers:
            print("Seat already reserved.")
        else:
            self.passengers[seat_number] = name
            print("Seat reserved for", name)

    def cancel_reservation(self):
        seat_number = input("Enter seat number to cancel reservation: ")

        if seat_number in self.passengers:
            del self.passengers[seat_number]
            print("Reservation canceled.")
        else:
            print("Seat is not reserved.")

    def display_passengers(self):
        print("Passengers:")
        for seat_number, name in self.passengers.items():
            print("Seat:", seat_number, "Name:", name)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.reserve_seat()
            elif choice == '2':
                self.cancel_reservation()
            elif choice == '3':
                self.display_passengers()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    flight_reservation_system = FlightReservationSystem()
    flight_reservation_system.run()
