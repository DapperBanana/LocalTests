
class FlightReservationSystem:
    def __init__(self):
        self.seats = [False] * 10
        
    def display_available_seats(self):
        print("Available Seats:")
        for idx, seat in enumerate(self.seats):
            if not seat:
                print(f"Seat {idx+1} is available")
                
    def make_reservation(self):
        self.display_available_seats()
        seat_num = int(input("Enter seat number to reserve: "))
        if self.seats[seat_num - 1]:
            print("Seat already reserved. Please choose another seat.")
        else:
            self.seats[seat_num - 1] = True
            print(f"Seat {seat_num} reserved successfully.")
    
    def cancel_reservation(self):
        seat_num = int(input("Enter seat number to cancel reservation: "))
        if not self.seats[seat_num - 1]:
            print("Seat is not reserved. No need to cancel.")
        else:
            self.seats[seat_num - 1] = False
            print(f"Reservation for seat {seat_num} cancelled.")
    
    def display_menu(self):
        while True:
            print("\nFlight Reservation System Menu:")
            print("1. Display available seats")
            print("2. Make a reservation")
            print("3. Cancel reservation")
            print("4. Quit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.display_available_seats()
            elif choice == '2':
                self.make_reservation()
            elif choice == '3':
                self.cancel_reservation()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    frs = FlightReservationSystem()
    frs.display_menu()
