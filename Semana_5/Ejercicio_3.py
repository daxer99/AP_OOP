class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

class Theater:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

class Showtime:
    def __init__(self, movie, theater, time):
        self.movie = movie
        self.theater = theater
        self.time = time

class Booking:
    def __init__(self, showtime, seats):
        self.showtime = showtime
        self.seats = seats

    def calculate_cost(self):
        return len(self.seats) * self.showtime.movie.rating

    def print_ticket(self):
        print("Movie: ", self.showtime.movie.title)
        print("Theater: ", self.showtime.theater.name)
        print("Time: ", self.showtime.time)
        print("Seats: ", self.seats)
        print("Cost: ", self.calculate_cost())

# Example Usage
movie1 = Movie("Avengers: Endgame", "Action", 9.0)
theater1 = Theater("AMC Theater", "New York", 100)
showtime1 = Showtime(movie1, theater1, "9:00 PM")

booking1 = Booking(showtime1, ["A1", "A2", "A3"])
booking1.print_ticket()