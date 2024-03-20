from __init__ import CONN,CURSOR
class Flight:
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
