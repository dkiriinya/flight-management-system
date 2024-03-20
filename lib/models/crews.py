class Crew:
    all = {}
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
        else:
            raise ValueError("flight_id must be an existing Flight ID")
            
    @classmethod
    def find_by_id(cls, id):
        """Return a Crew object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM crews
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS crews (
            id INTEGER PRIMARY KEY,
            name TEXT,
            role TEXT,
            experience_level TEXT,
            flight_id INTEGER,
            FOREIGN KEY (flight_id) REFERENCES flights(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS crews;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        sql = """
            INSERT INTO crews (name, role, experience_level, flight_id)
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.role, self.experience_level, self.flight_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod    
    def create(cls, name, role, experience_level, flight_id):
        crew = cls(name, role, experience_level, flight_id)
        crew.save()
        return crew
    
    def update(self):
        sql = """
            UPDATE crews
            SET name= ?, role = ?,  experience_level = ?, flight_id = ?
            WHERE id = ?
        """
        
        CURSOR.execute(sql,(self.name,self.role,self.experience_level,self.flight_id,self.id))
        CONN.commit()
        
    def delete(self):
        sql = """
            DELETE FROM crews
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    
    @classmethod
    def instance_from_db(cls, row):
        crew = cls.all.get(row[0])
        if crew:
            crew.name = row[1]
            crew.role = row[2]
            crew.experience = row[3]
            crew.flight_id = row[4]
        
        else:
            crew = cls(row[1],row[2],row[3],row[4])
            crew.id = row[0]
            cls.all[crew.id] = crew
            
        return crew

from flights import Flight
from __init__ import CONN,CURSOR