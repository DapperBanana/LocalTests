
class FlightReservationSystem:
    def __init__(self):
        self.seats = [False] * 10
    
    def display_available_seats(self):
        print("\nAvailable Seats:")
        for i, seat in enumerate(self.seats, start=1):
            if not seat:
                print(f"Seat {i} is available")
            else:
                print(f"Seat {i} is taken")
    
    def reserve_seat(self, seat_number):
        if self.seats[seat_number - 1]:
            print(f"Seat {seat_number} is already taken. Please choose another seat.")
        else:
            self.seats[seat_number - 1] = True
            print(f"Seat {seat_number} has been successfully reserved.")
    
    def cancel_reservation(self, seat_number):
        if not self.seats[seat_number - 1]:
            print(f"Seat {seat_number} is not reserved. No need to cancel.")
        else:
            self.seats[seat_number - 1] = False
            print(f"Reservation for seat {seat_number} has been cancelled.")
            

def main():
    flight_system = FlightReservationSystem()

    while True:
        print("\nFlight Reservation System")
        print("1. Display available seats")
        print("2. Reserve a seat")
        print("3. Cancel reservation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_system.display_available_seats()
        elif choice == '2':
            seat_number = int(input("Enter seat number to reserve: "))
            flight_system.reserve_seat(seat_number)
        elif choice == '3':
            seat_number = int(input("Enter seat number to cancel reservation: "))
            flight_system.cancel_reservation(seat_number)
        elif choice == '4':
            print("Thank you for using the Flight Reservation System. Have a safe flight!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
