
class FlightReservation:
    def __init__(self):
        self.passenger_list = []

    def display_menu(self):
        print("1. Reserve a seat")
        print("2. Cancel reservation")
        print("3. View passenger list")
        print("4. Exit")

    def reserve_seat(self):
        name = input("Enter passenger name: ")
        seat_number = input("Enter seat number: ")
        self.passenger_list.append((name, seat_number))
        print("Seat reserved for", name)

    def cancel_reservation(self):
        name = input("Enter passenger name: ")
        for passenger in self.passenger_list:
            if passenger[0] == name:
                self.passenger_list.remove(passenger)
                print("Reservation canceled for", name)
                return
        print("Passenger not found")

    def view_passenger_list(self):
        if not self.passenger_list:
            print("No reservations made yet")
        else:
            for passenger in self.passenger_list:
                print(passenger[0], " - Seat:", passenger[1])

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                self.reserve_seat()
            elif choice == '2':
                self.cancel_reservation()
            elif choice == '3':
                self.view_passenger_list()
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again")


if __name__ == "__main__":
    flight_reservation = FlightReservation()
    flight_reservation.run()
