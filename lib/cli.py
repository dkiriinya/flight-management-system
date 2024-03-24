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
import os
from colorama import Fore, Style
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    clear_screen()
    print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
    exit()

def print_error(message):
    print(Fore.RED + "Error:", message + Style.RESET_ALL)

def print_success(message):
    print(Fore.GREEN + "Success:", message + Style.RESET_ALL)

def menu():
    print("Welcome to Airline Management System")
    print("-----------------------------------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all crew")
    print("2. Find crew by name")
    print("3. Find crew by id")
    print("4. Create a new crew")
    print("5. Update a crew")
    print("6. Delete a crew")
    print("7. List all flights")  
    print("8. Find flight by flight number")
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
    print("-----------------------------------")

def main():
    while True:
        clear_screen()
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_crews()
        elif choice == "2":
            find_crew_by_name()
        elif choice == "3":
            find_crew_by_id()
        elif choice == "4":
            create_crew()
        elif choice == "5":
            update_crew()
        elif choice == "6":
            delete_crew()
        elif choice == "7":  
            list_flights()
        elif choice == "8": 
            find_by_flight_number()
        elif choice == "9": 
            find_flight_by_id()
        elif choice == "10":  
            create_flight()
        elif choice == "11": 
            update_flight()
        elif choice == "12":  
            delete_flight()
        elif choice == "13":
            passengers_in_flight()
        elif choice == "14":
            crew_in_flight()
        elif choice == "15":  
            list_passengers()
        elif choice == "16": 
            find_passenger_by_name()
        elif choice == "17": 
            find_passenger_by_id()
        elif choice == "18":  
            create_passenger()
        elif choice == "19": 
            update_passenger()
        elif choice == "20":  
            delete_passenger()
        else:
            print_error("Invalid choice. Please select a valid option.")
            input("Press Enter to continue...")
        time.sleep(5)

if __name__ == "__main__":
    main()