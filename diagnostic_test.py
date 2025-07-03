
# Dictionary to store available flights
flights = {
    1: 'New York to Los Angeles',
    2: 'Chicago to Miami',
    3: 'San Francisco to Seattle'
}

# Dictionary to store seat availability for each flight
availability = {
    1: 10,
    2: 15,
    3: 20
}

def display_flights():
    print("Available flights:")
    for key, value in flights.items():
        print(f"{key}. {value}")

def book_flight():
    display_flights()
    flight_choice = int(input("Select a flight to book (1-3): "))
    
    if flight_choice not in flights:
        print("Invalid choice. Please select a valid flight.")
        return
    
    if availability[flight_choice] > 0:
        availability[flight_choice] -= 1
        print("Flight booked successfully!")
    else:
        print("Sorry, this flight is fully booked.")

def main():
    while True:
        print("\nWelcome to the flight reservation system")
        print("1. Display available flights")
        print("2. Book a flight")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            display_flights()
        elif choice == '2':
            book_flight()
        elif choice == '3':
            print("Thank you for using the flight reservation system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
