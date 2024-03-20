class Crew:
    def __init__(self, name, role, experience_level, flight_id, id=None):
        self.id = id
        self.name = name
        self.role = role
        self.experience_level = experience_level
        self.flight_id = flight_id
        
    def __repr__(self):
        return f"<Crew {self.id}: Name: {self.name}, Role: {self.role}, Experience Level: {self.experience_level}, Flight ID: {self.flight_id}>"
        
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
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        if isinstance(value, str) and len(value):
            self._role = value
        else:
            raise ValueError("role must be a non-empty string")
            
    @property
    def experience_level(self):
        return self._experience_level
    
    @experience_level.setter
    def experience_level(self, value):
        if isinstance(value, str) and len(value):
            self._experience_level = value
        else:
            raise ValueError("experience_level must be a non-empty string")
    
    @property
    def flight_id(self):
        return self._flight_id
    
    @flight_id.setter
    def flight_id(self, value):
        if type(value) is int and Flight.find_by_id(value):
            self._flight_id = value
        
from flights import Flight
