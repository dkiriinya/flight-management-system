def initialize_database():
    # Drop existing tables if they exist
    Crew.drop_table()
    Flight.drop_table()
    Passenger.drop_table()
    
    # Create new tables
    Crew.create_table()
    Flight.create_table()
    Passenger.create_table()
    
    # Create initial data
    flight1 = Flight.create("ABC123", "JFK", "2024-03-20 08:00", "2024-03-20 10:00", 200)
    flight2 = Flight.create("XYZ456", "LAX", "2024-03-21 12:00", "2024-03-21 15:00", 300)
    flight3 = Flight.create("DEF789", "SFO", "2024-03-22 09:00", "2024-03-22 11:00", 250)
    
    crew1 = Crew.create("John Doe", "Pilot", "Senior", flight1.id)
    crew2 = Crew.create("Jane Smith", "Flight Attendant", "Junior", flight2.id)
    crew3 = Crew.create("Emily Brown", "Co-Pilot", "Intermediate", flight3.id)
    
    passenger1 = Passenger.create("Alice Johnson", 25, "AB123456", flight1.id)
    passenger2 = Passenger.create("Bob Smith", 30, "CD789012", flight2.id)
    passenger3 = Passenger.create("Charlie Davis", 40, "EF345678", flight3.id)
    passenger4 = Passenger.create("David Wilson", 35, "GH901234", flight1.id)
    passenger5 = Passenger.create("Ella Miller", 28, "IJ567890", flight2.id)
    
    print("Initialized database with seed data")

# Import the required models and run the function
from models.crews import Crew
from models.flights import Flight
from models.passengers import Passenger


initialize_database()
