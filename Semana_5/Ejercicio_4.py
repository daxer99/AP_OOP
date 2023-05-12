class Flight:
    def __init__(self, flight_number, origin, destination, duration, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
        else:
            print("Flight is full!")

class Passenger:
    def __init__(self, name, email, passport):
        self.name = name
        self.email = email
        self.passport = passport

class Seat:
    def __init__(self, seat_number, is_reserved):
        self.seat_number = seat_number
        self.is_reserved = is_reserved

class Booking:
    def __init__(self, flight, passenger, seat):
        self.flight = flight
        self.passenger = passenger
        self.seat = seat

    def confirm_booking(self):
        if self.seat.is_reserved:
            print("Seat is already taken!")
        else:
            self.flight.add_passenger(self.passenger)
            self.seat.is_reserved = True
            print("Booking confirmed!")

# Example Usage
flight1 = Flight("AI101", "New York", "London", 10, 100)
passenger1 = Passenger("John Smith", "john.smith@example.com", "123456")
seat1 = Seat("A1", False)

booking1 = Booking(flight1, passenger1, seat1)
booking1.confirm_booking()