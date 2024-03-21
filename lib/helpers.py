from models.crews import Crew
from models.flights import Flight
from models.passengers import Passenger
import os
from colorama import Fore, Style
from tabulate import tabulate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def exit_program():
   clear_screen()
   print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
   exit()
    
def list_crews():
    crews = Crew.get_all()
    headers = ["ID", "Name", "Role", "Experience Level", "Flight ID"]
    data = [(crew.id, crew.name, crew.role, crew.experience_level, crew.flight_id) for crew in crews]
    print(tabulate(data, headers=headers, tablefmt="grid"))
        
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
    flight_id = int(input("Enter the crew member's flight_id: "))
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
    headers = ["ID", "Flight Number", "Departure Airport", "Departure Time", "Arrival Time", "Ticket Price"]
    data = [(flight.id, flight.flight_number, flight.departure_airport, flight.departure_time, flight.arrival_time, flight.ticket_price) for flight in flights]
    print(tabulate(data, headers=headers, tablefmt="grid"))


def find_by_flight_number():
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
        
def passengers_in_flight():
    _id = int(input("What is the flight ID: "))
    flight = Flight.find_by_id(_id)
    for passenger in flight.passengers():
        print(passenger)
        
def crew_in_flight():
    _id = int(input("What is the flight ID: "))
    flight = Flight.find_by_id(_id)
    for crew in flight.crews():
        print(crew)
        
def list_passengers():
    passengers = Passenger.get_all()
    headers = ["ID", "Name", "Age", "Passport Number", "Flight ID"]
    data = [(passenger.id, passenger.name, passenger.age, passenger.passport_number, passenger.flight_id) for passenger in passengers]
    print(tabulate(data, headers=headers, tablefmt="grid"))
        
def find_passenger_by_name():
    name = input("Enter passenger's name: ")
    passenger = Passenger.find_by_name(name)
    print(passenger) if passenger else print(
        f'Passenger {name} not found'
    )
    
def find_passenger_by_id():
    id_ = input("Enter the passenger's id: ")
    passenger = Passenger.find_by_id(id_)
    print(passenger) if passenger else print(f'Passenger {id_} not found')
    
def create_passenger():
    name = input("Enter the passenger's name: ")
    age = int(input("Enter the passenger's age: "))
    passport_number = input("Enter the passengers passport_number: ")
    flight_id = int(input("Enter the passengers's flight_id: "))
    try:
        passenger = Passenger.create(name,age,passport_number,flight_id)
        print(f'Success: {passenger}')
    except Exception as exc:
        print("Error creating Passenger: ",exc)
        

def update_passenger():
     id_ = input("Enter the passenger's id: ")
     if passenger := Passenger.find_by_id(id_):
        try:
            name = input("Enter the passenger's name: ")
            passenger.name = name
            age = int(input("Enter the passenger's age: "))
            passenger.age = age
            passport_number = input("Enter the passengers passport_number: ")
            passenger.passport_number = passport_number
            flight_id = int(input("Enter the crew member's flight_id: "))
            passenger.flight_id = flight_id
            
             
            passenger.update()
            print(f'Success: {passenger}')
        except Exception as exc:
            print("Error updating passenger: ",exc)
            
def delete_passenger():
    id_ = input("Enter the passenger's id: ")
    if passenger:= Passenger.find_by_id(id_):
        passenger.delete()
        print(f"Passenger {id_} deleted.")
    else:
        print(f'Passenger {id_} not found')