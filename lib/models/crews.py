class Crew:
    # Class variable to store all instances of Crew
    all = {}
    
    def __init__(self, name, role, experience_level, flight_id, id=None):
        """Initialize Crew instance with the given attributes."""
        self.id = id
        self.name = name
        self.role = role
        self.experience_level = experience_level
        self.flight_id = flight_id
        
    def __repr__(self):
        """String representation of the Crew instance."""
        return f"<Crew {self.id}: Name: {self.name}, Role: {self.role}, Experience Level: {self.experience_level}, Flight ID: {self.flight_id}>"
        
    @property
    def name(self):
        """Getter for name attribute."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name attribute with validation."""
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("name must be a non-empty string")
            
    @property
    def role(self):
        """Getter for role attribute."""
        return self._role
    
    @role.setter
    def role(self, value):
        """Setter for role attribute with validation."""
        if isinstance(value, str) and len(value):
            self._role = value
        else:
            raise ValueError("role must be a non-empty string")
            
    @property
    def experience_level(self):
        """Getter for experience_level attribute."""
        return self._experience_level
    
    @experience_level.setter
    def experience_level(self, value):
        """Setter for experience_level attribute with validation."""
        if isinstance(value, str) and len(value):
            self._experience_level = value
        else:
            raise ValueError("experience_level must be a non-empty string")
    
    @property
    def flight_id(self):
        """Getter for flight_id attribute."""
        return self._flight_id
    
    @flight_id.setter
    def flight_id(self, value):
        """Setter for flight_id attribute with validation."""
        if isinstance(value, int) and Flight.find_by_id(value):
            self._flight_id = value
        else:
            raise ValueError("flight_id must be an existing Flight ID")
            
    @classmethod
    def find_by_id(cls, id):
        """Return a Crew object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT *
            FROM crews
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def create_table(cls):
        """Create the crews table in the database if it doesn't exist."""
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
        """Drop the crews table from the database if it exists."""
        sql = """
            DROP TABLE IF EXISTS crews;
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    def save(self):
        """Save the Crew instance to the database."""
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
        """Create a new Crew instance and save it to the database."""
        crew = cls(name, role, experience_level, flight_id)
        crew.save()
        return crew
    
    def update(self):
        """Update the Crew instance in the database."""
        sql = """
            UPDATE crews
            SET name= ?, role = ?,  experience_level = ?, flight_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.role, self.experience_level, self.flight_id, self.id))
        CONN.commit()
        
    def delete(self):
        """Delete the Crew instance from the database."""
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
        """Create a Crew instance from a database row."""
        crew = cls.all.get(row[0])
        if crew:
            crew.name = row[1]
            crew.role = row[2]
            crew.experience = row[3]
            crew.flight_id = row[4]
        else:
            crew = cls(row[1], row[2], row[3], row[4])
            crew.id = row[0]
            cls.all[crew.id] = crew
            
        return crew
    
    @classmethod
    def get_all(cls):
        """Return a list of all Crew instances from the database."""
        sql = """
            SELECT *
            FROM crews
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Crew object corresponding to the first table row matching the specified name."""
        sql = """
            SELECT *
            FROM crews
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

# Importing required modules
from models.flights import Flight
from models.__init__ import CONN, CURSOR
