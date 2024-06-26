
class FlightReservationSystem:
    def __init__(self):
        self.passenger_list = []
        self.seat_map = {}

    def check_seat_availability(self, seat_number):
        return seat_number in self.seat_map and self.seat_map[seat_number] == ""

    def reserve_seat(self, passenger_name, seat_number):
        if not self.check_seat_availability(seat_number):
            print("Seat {} is already taken. Please choose another seat.".format(seat_number))
            return
        
        self.seat_map[seat_number] = passenger_name
        self.passenger_list.append((passenger_name, seat_number))
        print("Seat {} reserved for passenger {}.".format(seat_number, passenger_name))

    def cancel_reservation(self, passenger_name, seat_number):
        if (passenger_name, seat_number) in self.passenger_list:
            self.seat_map[seat_number] = ""
            self.passenger_list.remove((passenger_name, seat_number))
            print("Reservation for passenger {} at seat {} canceled.".format(passenger_name, seat_number))
        else:
            print("No reservation found for passenger {} at seat {}.".format(passenger_name, seat_number))

    def display_passenger_list(self):
        for passenger_name, seat_number in self.passenger_list:
            print("Passenger: {}, Seat: {}".format(passenger_name, seat_number))

    def display_seat_map(self):
        for seat_number, passenger_name in self.seat_map.items():
            status = "Available" if passenger_name == "" else "Taken by {}".format(passenger_name)
            print("Seat {}: {}".format(seat_number, status))

def main():
    flight_system = FlightReservationSystem()
    while True:
        print("\nFlight Reservation System:")
        print("1. Reserve Seat")
        print("2. Cancel Reservation")
        print("3. Display Passenger List")
        print("4. Display Seat Map")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            passenger_name = input("Enter passenger name: ")
            seat_number = input("Enter seat number: ")
            flight_system.reserve_seat(passenger_name, seat_number)
        elif choice == "2":
            passenger_name = input("Enter passenger name: ")
            seat_number = input("Enter seat number: ")
            flight_system.cancel_reservation(passenger_name, seat_number)
        elif choice == "3":
            flight_system.display_passenger_list()
        elif choice == "4":
            flight_system.display_seat_map()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
