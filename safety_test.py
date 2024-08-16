
class FlightReservationSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight_number, source, destination, capacity):
        self.flights[flight_number] = {'source': source, 'destination': destination, 'capacity': capacity, 'passengers': []}

    def display_available_flights(self):
        print("Available Flights:")
        for flight_number, flight_info in self.flights.items():
            seats_available = flight_info['capacity'] - len(flight_info['passengers'])
            print(f"Flight: {flight_number}, Source: {flight_info['source']}, Destination: {flight_info['destination']}, Remaining Seats: {seats_available}")

    def reserve_seat(self, flight_number, passenger_name):
        if flight_number in self.flights:
            flight_info = self.flights[flight_number]
            if len(flight_info['passengers']) < flight_info['capacity']:
                flight_info['passengers'].append(passenger_name)
                print(f"Seat reserved for {passenger_name} on flight {flight_number}")
            else:
                print("Sorry, the flight is fully booked.")
        else:
            print("Invalid flight number.")

# Create a flight reservation system object
frs = FlightReservationSystem()

# Add some flights to the system
frs.add_flight('F001', 'New York', 'London', 100)
frs.add_flight('F002', 'Paris', 'Tokyo', 150)
frs.add_flight('F003', 'Sydney', 'Dubai', 200)

# Display available flights
frs.display_available_flights()

# Reserve a seat on a flight
frs.reserve_seat('F002', 'Alice')

# Display available flights again
frs.display_available_flights()
