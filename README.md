# Flight Management System

## Overview

The Flight Management System is a Python-based application designed to manage flights, crews, and passengers for an airline company. It utilizes SQLite3 as a database to store and manage the data.

---

## Features

### Crew Management
- List all crew members
- Find crew by name
- Find crew by ID
- Create a new crew
- Update a crew
- Delete a crew

### Flight Management
- List all flights
- Find flight by flight number
- Find flight by ID
- Create a new flight
- Update a flight
- Delete a flight
- List all passengers in a flight
- List all crew in a flight

### Passenger Management
- List all passengers
- Find passenger by name
- Find passenger by ID
- Create a new passenger
- Update a passenger
- Delete a passenger

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dkiriinya/flight-management-system.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd flight-management-system
    ```

3. Run the application:
    ```bash
    python lib/cli.py
    ```

---

## Database Schema

### Crews Table

```sql
CREATE TABLE IF NOT EXISTS crews (
    id INTEGER PRIMARY KEY,
    name TEXT,
    role TEXT,
    experience_level TEXT,
    flight_id INTEGER,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);
```

### Flights Table

```sql
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY,
    flight_number TEXT,
    departure_airport TEXT,
    departure_time TEXT,
    arrival_time TEXT,
    ticket_price INTEGER
);
```

### Passengers Table

```sql
CREATE TABLE IF NOT EXISTS passengers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    passport_number TEXT,
    flight_id INTEGER,
    FOREIGN KEY (flight_id) REFERENCES flights(id)
);
```

---

## Usage

Upon running the application, you will be presented with a menu to perform various operations related to crew, flights, and passengers.

### Menu Options

- List all crew
- Find crew by name
- Find crew by ID
- Create a new crew
- Update a crew
- Delete a crew
- List all flights
- Find flight by flight number
- Find flight by ID
- Create a new flight
- Update a flight
- Delete a flight
- List all passengers in a flight
- List all crew in a flight
- List all passengers
- Find passenger by name
- Find passenger by ID
- Create a new passenger
- Update a passenger
- Delete a passenger

---

## Contributors

- [Don Kiriinya](https://github.com/dkiriinya)

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit) file for details.



