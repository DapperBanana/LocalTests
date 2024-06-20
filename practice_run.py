
def display_menu():
    print("Welcome to the flight reservation system!")
    print("1. Display available flights")
    print("2. Reserve a flight")
    print("3. Cancel reservation")
    print("4. Exit")
    
def display_flights():
    print("Available flights:")
    print("1. Flight 123 - New York to Los Angeles")
    print("2. Flight 456 - Chicago to Miami")
    
def reserve_flight():
    print("Enter your name:")
    name = input()
    print("Enter the flight number you want to reserve:")
    flight_number = input()
    print("Reservation confirmed for {} on flight {}.".format(name, flight_number))
    
def cancel_reservation():
    print("Enter your name to cancel your reservation:")
    name = input()
    print("Reservation cancelled for {}.".format(name))
    
while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_flights()
    elif choice == "2":
        reserve_flight()
    elif choice == "3":
        cancel_reservation()
    elif choice == "4":
        print("Thank you for using the flight reservation system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
