
class Passenger:
    all = {}
    def __init__(self, name, age, passport_number, flight_id):
        self.name = name
        self.age = age
        self.passport_number = passport_number
        self.flight_id = flight_id
        
    def __repr__(self):
        return f"<Passenger: Name: {self.name}, Age: {self.age}, Passport Number: {self.passport_number}, Flight ID: {self.flight_id}>"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("name must be a non-empty string")
            
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("age must be a positive integer")
            
    @property
    def passport_number(self):
        return self._passport_number
    
    @passport_number.setter
    def passport_number(self, value):
        if isinstance(value, str) and len(value):
            self._passport_number = value
        else:
            raise ValueError("passport_number must be a non-empty string")
            
    @property
    def flight_id(self):
        return self._flight_id
    
    @flight_id.setter
    def flight_id(self, value):
        if type(value) is int and Flight.find_by_id(value):
            self._flight_id = value
        else:
            raise ValueError("flight_id must be an existing Flight ID")
            
    @classmethod
    def find_by_id(cls, id):
        """Return a Passenger object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM passengers
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS passengers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            passport_number TEXT,
            flight_id INTEGER,
            FOREIGN KEY (flight_id) REFERENCES flights(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS passengers;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO passengers (name, age, passport_number, flight_id)
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.passport_number, self.flight_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
    @classmethod    
    def create(cls, name, age, passport_number, flight_id):
        passenger = cls(name, age, passport_number, flight_id)
        passenger.save()
        return passenger
    
    def update(self):
        sql = """
            UPDATE passengers
            SET name = ?, age = ?, passport_number = ?, flight_id = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql, (self.name, self.age, self.passport_number, self.flight_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM passengers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None
        
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM crews
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Passenger object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM passengers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Passenger object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM passengers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def instance_from_db(cls, row):
        passenger = cls.all.get(row[0])
        if passenger:
            passenger.name = row[1]
            passenger.age = row[2]
            passenger.passport_number = row[3]
            passenger.flight_id = row[4]
        
        else:
            passenger = cls(row[1],row[2],row[3],row[4])
            passenger.id = row[0]
            cls.all[passenger.id] = passenger
            
        return passenger

from models.__init__ import CONN, CURSOR
from models.flights import Flight
