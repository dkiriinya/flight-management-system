from helpers import exit_program,list_crews,find_crew_by_name,find_crew_by_id,create_crew,update_crew,delete_crew,list_flights,find_by_fight_number,find_flight_by_id,create_flight,update_flight,delete_flight

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
            find_flight_by_id()
        if choice == "9":  
            create_flight()
        if choice == "10": 
            update_flight()
        if choice == "11":  
            delete_flight()


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
    print("8. Find flight by id")  
    print("9. Create a new flight")  
    print("10. Update a flight")  
    print("11. Delete a flight")  


if __name__ == "__main__":
    main()
