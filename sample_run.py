
# Simple flight reservation system

# Function to display the menu options
def display_menu():
    print("--------------------------")
    print("Flight Reservation System")
    print("--------------------------")
    print("1. Search Flights")
    print("2. Reserve a Flight")
    print("3. Cancel Reservation")
    print("4. Exit")
    print("--------------------------")

# Function to search for available flights
def search_flights():
    print("Available Flights:")
    print("1. Flight 001 - New York to Los Angeles")
    print("2. Flight 002 - Chicago to Miami")
    print("3. Flight 003 - Atlanta to Dallas")

# Function to reserve a flight
def reserve_flight():
    flight_number = int(input("Enter the flight number you want to reserve: "))
    print(f"Flight {flight_number} reserved successfully!")

# Function to cancel a reservation
def cancel_reservation():
    print("Reservation cancelled successfully!")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            search_flights()
        
        elif choice == 2:
            reserve_flight()

        elif choice == 3:
            cancel_reservation()

        elif choice == 4:
            print("Thank you for using the Flight Reservation System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
