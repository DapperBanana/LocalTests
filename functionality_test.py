
class FlightReservationSystem:
    def __init__(self):
        self.seats = [False] * 10

    def display_available_seats(self):
        print("Available seats:")
        for i in range(len(self.seats)):
            if not self.seats[i]:
                print(f"Seat {i+1} is available")
        print()

    def reserve_seat(self, seat_num):
        if 1 <= seat_num <= 10:
            if not self.seats[seat_num-1]:
                self.seats[seat_num-1] = True
                print(f"Seat {seat_num} reserved successfully!")
            else:
                print(f"Seat {seat_num} is already taken. Please choose another seat.")
        else:
            print("Invalid seat number. Seat number must be between 1 and 10.")

    def cancel_reservation(self, seat_num):
        if 1 <= seat_num <= 10:
            if self.seats[seat_num-1]:
                self.seats[seat_num-1] = False
                print(f"Reservation for seat {seat_num} cancelled.")
            else:
                print(f"No reservation found for seat {seat_num}.")
        else:
            print("Invalid seat number. Seat number must be between 1 and 10.")

# Main program
flight_reservation_system = FlightReservationSystem()

while True:
    print("Welcome to the Flight Reservation System")
    print("1. Display available seats")
    print("2. Reserve a seat")
    print("3. Cancel reservation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        flight_reservation_system.display_available_seats()
    elif choice == '2':
        seat_num = int(input("Enter seat number to reserve: "))
        flight_reservation_system.reserve_seat(seat_num)
    elif choice == '3':
        seat_num = int(input("Enter seat number to cancel reservation: "))
        flight_reservation_system.cancel_reservation(seat_num)
    elif choice == '4':
        print("Thank you for using the Flight Reservation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
