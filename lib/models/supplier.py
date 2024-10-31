# lib/models/supplier.py
from . import CURSOR, CONN

class Supplier:
    def __init__(self, supplier_id=None, name="", contact_information="", location=""):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_information = contact_information
        self.location = location

    @classmethod
    def create_table(cls):
        """Create the suppliers table if it doesn't exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                contact_information TEXT,
                location TEXT
            )
        ''')
        CONN.commit()

    def save(self):
        """Save a new supplier to the database."""
        CURSOR.execute('''
            INSERT INTO suppliers (name, contact_information, location)
            VALUES (?, ?, ?)
        ''', (self.name, self.contact_information, self.location))
        CONN.commit()

    @classmethod
    def find_by_id(cls, supplier_id):
        """Find a supplier by ID."""
        CURSOR.execute('SELECT * FROM suppliers WHERE supplier_id = ?', (supplier_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
    
    @classmethod
    def all(cls):
        """Fetch all suppliers from the database."""
        CURSOR.execute("SELECT * FROM suppliers")
        rows = CURSOR.fetchall()
        suppliers = [cls(*row) for row in rows]  # assuming __init__ matches the table structure
        return suppliers
    

    # Additional methods for updating and deleting can be added here
