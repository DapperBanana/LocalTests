
flights = {
    "AA101": {
        "origin": "New York",
        "destination": "Los Angeles",
        "departure_time": "10:00",
        "arrival_time": "13:00",
        "available_seats": 50
    },
    "UA202": {
        "origin": "Chicago",
        "destination": "Miami",
        "departure_time": "12:00",
        "arrival_time": "15:00",
        "available_seats": 80
    },
    "DL303": {
        "origin": "Dallas",
        "destination": "Denver",
        "departure_time": "14:00",
        "arrival_time": "16:30",
        "available_seats": 40
    }
}

def display_flights():
    print("Available Flights:")
    for flight, details in flights.items():
        print(flight, details["origin"], "->", details["destination"], "Departure:", details["departure_time"])

def make_reservation(flight):
    if flight in flights:
        if flights[flight]["available_seats"] > 0:
            flights[flight]["available_seats"] -= 1
            print("Reservation made for Flight", flight)
        else:
            print("Sorry, no available seats for this flight.")
    else:
        print("Invalid flight number.")

display_flights()

user_choice = input("Enter flight number to make a reservation: ")
make_reservation(user_choice)
