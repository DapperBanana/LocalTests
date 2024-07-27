
# Define a list of available flights
flights = ["Flight 1 - New York to Los Angeles",
           "Flight 2 - Chicago to Miami",
           "Flight 3 - Boston to San Francisco"]

# Define a dictionary to store reservations
reservations = {}

# Function to display available flights
def display_flights():
    print("Available Flights:")
    for i, flight in enumerate(flights):
        print(f"{i+1}. {flight}")

# Function to make a reservation
def make_reservation():
    display_flights()
    flight_number = int(input("Enter flight number to make a reservation: "))
    name = input("Enter your name: ")
    reservations[name] = flights[flight_number - 1]
    print(f"Reservation made successfully for {name} on {flights[flight_number - 1]}")

# Function to display reservations
def display_reservations():
    print("Reservations:")
    for name, flight in reservations.items():
        print(f"{name} - {flight}")

# Main loop
while True:
    print("\nFlight Reservation System")
    print("1. Display available flights")
    print("2. Make a reservation")
    print("3. Display reservations")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_flights()
    elif choice == '2':
        make_reservation()
    elif choice == '3':
        display_reservations()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
