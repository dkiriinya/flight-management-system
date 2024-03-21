
def initialize_database():
    Crew.drop_table()
    Flight.drop_table()
    Passenger.drop_table()
    Crew.create_table()
    Flight.create_table()
    Passenger.create_table()
    
    # Create initial data
    flight1 = Flight.create("ABC123", "JFK", "2024-03-20 08:00", "2024-03-20 10:00", 200)
    flight2 = Flight.create("XYZ456", "LAX", "2024-03-21 12:00", "2024-03-21 15:00", 300)
    
    crew1 = Crew.create("John Doe", "Pilot", "Senior", flight1.id)
    crew2 = Crew.create("Jane Smith", "Flight Attendant", "Junior", flight2.id)
    
    passenger1 = Passenger.create("Alice Johnson", 25, "AB123456", flight1.id)
    passenger2 = Passenger.create("Bob Smith", 30, "CD789012", flight2.id)
    
    
from models.crews import Crew
from models.flights import Flight
from models.passengers import Passenger

initialize_database()
print("Initialized database with seed data")


    
