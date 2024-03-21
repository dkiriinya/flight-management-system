from helpers import (exit_program,list_crews,
                     find_crew_by_name,find_crew_by_id,
                     create_crew,update_crew,delete_crew,
                     list_flights,find_by_flight_number,
                     find_flight_by_id,create_flight,
                     update_flight,delete_flight,
                     passengers_in_flight,crew_in_flight,
                     list_passengers,find_passenger_by_name,
                     find_passenger_by_id,create_passenger,
                     update_passenger,delete_passenger)



def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        if choice == "1":
            list_crews()
        if choice == "2":
            find_crew_by_name()
        if choice == "3":
            find_crew_by_id()
        if choice == "4":
            create_crew()
        if choice == "5":
            update_crew()
        if choice == "6":
            delete_crew()
        if choice == "7":  
            list_flights()
        if choice == "8": 
            find_by_flight_number()
        if choice == "9": 
            find_flight_by_id()
        if choice == "10":  
            create_flight()
        if choice == "11": 
            update_flight()
        if choice == "12":  
            delete_flight()
        if choice == "13":
            passengers_in_flight()
        if choice == "14":
            crew_in_flight()
        if choice == "15":  
            list_passengers()
        if choice == "16": 
            find_passenger_by_name()
        if choice == "17": 
            find_passenger_by_id()
        if choice == "18":  
            create_passenger()
        if choice == "19": 
            update_passenger()
        if choice == "20":  
            delete_passenger()


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all crew")
    print("2. Find crew by name")
    print("3. Find crew by id")
    print("4. Create a new crew")
    print("5. Update a crew")
    print("6. Delete a crew")
    print("7. List all flights")  
    print("8. Find flight by name")
    print("9. Find flight by id")  
    print("10. Create a new flight")  
    print("11. Update a flight")  
    print("12. Delete a flight")
    print("13. List all passengers in a flight")  
    print("14. List all crew in a flight")  
    print("15. List all passengers")  
    print("16. Find passenger by name")
    print("17. Find passenger by id")  
    print("18. Create a new passenger")  
    print("19. Update a passenger")  
    print("20. Delete a passenger")  


if __name__ == "__main__":
    main()
