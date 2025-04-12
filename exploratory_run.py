
class FlightReservationSystem:
    def __init__(self):
        self.seats = {'A': [False]*10, 'B': [False]*10, 'C': [False]*10}

    def display_seats(self):
        print("Current seat status:")
        print("Row A:", self.seats['A'])
        print("Row B:", self.seats['B'])
        print("Row C:", self.seats['C'])

    def reserve_seat(self, row, seat):
        if row not in self.seats or seat < 0 or seat >= len(self.seats[row]):
            print("Invalid seat selection. Please try again.")
            return False

        if self.seats[row][seat]:
            print("Seat is already reserved. Please select another seat.")
            return False

        self.seats[row][seat] = True
        print(f"Seat {row}{seat} reserved successfully.")
        return True

    def cancel_reservation(self, row, seat):
        if row not in self.seats or seat < 0 or seat >= len(self.seats[row]):
            print("Invalid seat selection. Please try again.")
            return False

        if not self.seats[row][seat]:
            print("Seat is not reserved. No need to cancel.")
            return False

        self.seats[row][seat] = False
        print(f"Reservation for seat {row}{seat} cancelled.")
        return True

# Main program
frs = FlightReservationSystem()
while True:
    print("\nMenu:")
    print("1. Display seat status")
    print("2. Reserve a seat")
    print("3. Cancel reservation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        frs.display_seats()
    elif choice == '2':
        row = input("Enter row (A, B, C): ")
        seat = int(input("Enter seat number (0-9): "))
        frs.reserve_seat(row, seat)
    elif choice == '3':
        row = input("Enter row (A, B, C): ")
        seat = int(input("Enter seat number (0-9): "))
        frs.cancel_reservation(row, seat)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
