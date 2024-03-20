class Flight:
    all = {}
    def __init__(self, flight_number, departure_airport, departure_time, arrival_time, ticket_price, id=None):
        self.id = id
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.ticket_price = ticket_price
        
    def __repr__(self):
        return (
            f"<Flight {self.id}: flight number: {self.flight_number}, Departure airport: {self.departure_airport} >" +
            f"Departure Time: {self.departure_time}, Arrival Time: {self.arrival_time}, Ticket Price: {self.ticket_price}"
        )
        
    @property
    def flight_number(self):
        return self._flight_number
    
    @flight_number.setter
    def flight_number(self, value):
        if isinstance(value, str) and len(value):
            self._flight_number = value
        else:
            raise ValueError("flight_number must be a non-empty string")
            
    @property
    def departure_airport(self):
        return self._departure_airport
    
    @departure_airport.setter
    def departure_airport(self, value):
        if isinstance(value, str) and len(value):
            self._departure_airport = value
        else:
            raise ValueError("departure_airport must be a non-empty string")
            
    @property
    def departure_time(self):
        return self._departure_time
    
    @departure_time.setter
    def departure_time(self, value):
        if isinstance(value, str) and len(value):
            self._departure_time = value
        else:
            raise ValueError("value must be a non-empty string")
        
    @property
    def arrival_time(self):
        return self._arrival_time
    
    @arrival_time.setter
    def arrival_time(self, value):
        if isinstance(value, str) and len(value):
            self._arrival_time = value
        else:
            raise ValueError("arrival_time must be a none-empty string")
        
    @property
    def ticket_price(self):
        return self._ticket_price
    
    @ticket_price.setter
    def ticket_price(self, value):
        if isinstance(value, int) and len(str(value)):
            self._ticket_price = value
        else:
            raise ValueError("ticket_price must be a non-empty integer")
    
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM flights
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def create_table(cls):
        # flight_number, departure_airport, departure_time, arrival_time, ticket_price
        sql = """
            CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY,
            flight_number TEXT,
            departure_airport TEXT,
            departure_time TEXT,
            arrival_time TEXT,
            ticket_price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod   
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS flights;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO flights (flight_number, departure_airport, departure_time, arrival_time, ticket_price)
            VALUES (?,?,?,?,?)
        """
        
        CURSOR.execute(sql,(self.flight_number,self.departure_airport,self.departure_time,self.arrival_time,self.ticket_price))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod    
    def create(cls,flight_number, departure_airport, departure_time, arrival_time, ticket_price):
        flight = cls(flight_number, departure_airport, departure_time, arrival_time, ticket_price)
        flight.save()
        return flight
    
    @classmethod
    def instance_from_db(cls, row):
        flight = cls.all.get(row[0])
        if flight:
            flight.flight_number = row[1]
            flight.departure_airport = row[2]
            flight.departure_time = row[3]
            flight.arrival_time = row[4]
            flight.ticket_price = row[5]
            
        else:
            flight = cls(row[1],row[2],row[3],row[4],row[5])
            flight.id = row[0]
            cls.all[flight.id] = flight
            
        return flight
            
            
from __init__ import CONN,CURSOR