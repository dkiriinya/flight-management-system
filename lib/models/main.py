from flights import Flight
from crews import Crew
from passengers import Passenger
def main():
# Create more flights
    flight3 = Flight.create("DEF789", "SFO", "2024-03-22 09:00", "2024-03-22 11:00", 250)
    flight4 = Flight.create("GHI101", "ORD", "2024-03-23 13:00", "2024-03-23 16:00", 350)

    # Create more crew members
    crew3 = Crew.create("Michael Johnson", "Co-pilot", "Junior", flight3.id)
    crew4 = Crew.create("Emily Brown", "Flight Attendant", "Senior", flight4.id)

    # Create more passengers
    passenger3 = Passenger.create("Carol Williams", 40, "EF234567", flight3.id)
    passenger4 = Passenger.create("David Jones", 50, "GH345678", flight4.id)
    
    for crew in flight3.crews():
        print (crew)
        
    for passenger in flight3.passengers():
        print (passenger)

main()