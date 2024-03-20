class Passenger:
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
            
from flights import Flight
