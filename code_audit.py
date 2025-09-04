
class FlightReservationSystem:
    def __init__(self):
        self.reservations = {}

    def make_reservation(self, name, seat_number):
        if seat_number in self.reservations:
            print("Sorry, seat is already taken. Please choose another seat.")
        else:
            self.reservations[seat_number] = name
            print(f"Reservation successful! {name} is booked in seat {seat_number}.")

    def cancel_reservation(self, name):
        for seat_number, passenger_name in self.reservations.items():
            if passenger_name == name:
                del self.reservations[seat_number]
                print(f"Reservation for {name} in seat {seat_number} has been cancelled.")
                return

        print("No reservation found for that passenger name.")

    def show_available_seats(self):
        for seat_number in range(1, 11):
            if seat_number not in self.reservations:
                print(f"Seat {seat_number} is available.")
            else:
                print(f"Seat {seat_number} is taken by {self.reservations[seat_number]}.")

system = FlightReservationSystem()

while True:
    print("\n1. Make Reservation")
    print("2. Cancel Reservation")
    print("3. Show Available Seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter passenger name: ")
        seat_number = int(input("Enter seat number to reserve: "))
        system.make_reservation(name, seat_number)
    elif choice == '2':
        name = input("Enter passenger name to cancel reservation: ")
        system.cancel_reservation(name)
    elif choice == '3':
        system.show_available_seats()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
