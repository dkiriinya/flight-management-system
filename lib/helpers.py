from models.crews import Crew
from models.flights import Flight
from models.passengers import Passenger

def exit_program():
    print("Goodbye!")
    exit()
    
def list_crews():
    crews = Crew.get_all()
    for crew in crews:
        print(crew)
        
def find_crew_by_name():
    name = input("Enter the crew member's name: ")
    crew = Crew.find_by_name(name)
    print(crew) if crew else print(
        f'Crew {name} not found'
    )
    
def find_crew_by_id():
    id_ = input("Enter the crew's id: ")
    crew = Crew.find_by_id(id_)
    print(crew) if crew else print(f'Crew {id_} not found')
    
def create_crew():
    name = input("Enter the crew member's name: ")
    role = input("Enter the crew member's role: ")
    experience_level = input("Enter the crew member's experience level: ")
    flight_id = input("Enter the crew member's flight_id: ")
    try:
        crew = Crew.create(name,role,experience_level,flight_id)
        print(f'Success: {crew}')
    except Exception as exc:
        print("Error creating Crew: ",exc)
        
def update_crew():
     id_ = input("Enter the crew's id: ")
     if crew := Crew.find_by_id(id_):
        try:
             name = input("Enter the crew member's name: ")
             crew.name = name
             role = input("Enter the crew member's role: ")
             crew.role = role
             experience_level = input("Enter the crew member's experience level: ")
             crew.experience_level = experience_level
             flight_id = int(input("Enter the crew member's flight_id: "))
             crew.flight_id = flight_id
             
             crew.update()
             print(f'Success: {crew}')
        except Exception as exc:
            print("Error updating crew: ",exc)
            
def delete_crew():
    id_ = input("Enter the crews's id: ")
    if crew := Crew.find_by_id(id_):
        crew.delete()
        print(f'Crew {id_} deleted')
    else:
        print(f'Crew {id_} not found')
        
def list_flights():
    flights = Flight.get_all()
    for flight in flights:
        print(flight)

def find_by_fight_number():
    flight_number = input("Enter the flight number: ")
    flight = Flight.find_by_flight_number(flight_number)
    print(flight) if flight else print(
        f'Flight number {flight_number} not found'
    )

def find_flight_by_id():
    id_ = input("Enter the flight's id: ")
    flight = Flight.find_by_id(id_)
    print(flight) if flight else print(f'Flight {id_} not found')
    
def create_flight():
    flight_number = input("Enter the flight number: ")
    departure_airport = input("Enter the departure airport: ")
    departure_time = input("Enter the departure_time: ")
    arrival_time = input("Enter the arrival time: ")
    ticket_price = int(input("Enter the ticket price: "))
    try:
        flight = Flight.create(flight_number,departure_airport,departure_time,arrival_time,ticket_price)
        print(f'Success: {flight}')
    except Exception as exc:
        print("Error creating Flight: ",exc)
        
def update_flight():
    id_ = input("Enter the flight's id: ")
    if flight:= Flight.find_by_id(id_):
        try:
            flight_number = input("Enter the flight number: ")
            flight.flight_number = flight_number
            departure_airport = input("Enter the departure airport: ")
            flight.departure_airport = departure_airport
            departure_time = input("Enter the departure_time: ")
            flight.departure_time = departure_time
            arrival_time = input("Enter the arrival time: ")
            flight.arrival_time = arrival_time
            ticket_price = int(input("Enter the ticket price: "))
            flight.ticket_price = ticket_price
            
            flight.update()
            print(f"success:{flight}")
        except Exception as exc:
            print("Erro updating Flight: ",exc)

def delete_flight():
    id_ = input("Enter the flight's id: ")
    if flight:= Flight.find_by_id(id_):
        flight.delete()
        print(f"Flight {id_} deleted.")
    else:
        print(f'Flight {id_} not found')