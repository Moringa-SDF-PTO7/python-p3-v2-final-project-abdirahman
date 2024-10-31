# lib/models/customer.py
from . import CURSOR, CONN

class Customer:
    def __init__(self, customer_id, name, contact_information):
        self.customer_id = customer_id
        self.name = name
        self.contact_information = contact_information

    @classmethod
    def create_table(cls):
        """Create the customers table if it doesn't exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                contact_information TEXT
            )
        ''')
        CONN.commit()

    def save(self):
        """Save a new customer to the database."""
        CURSOR.execute('''
            INSERT INTO customers (name, contact_information)
            VALUES (?, ?)
        ''', (self.name, self.contact_information))
        CONN.commit()

    @classmethod
    def find_by_id(cls, customer_id):
        """Find a customer by ID."""
        CURSOR.execute('SELECT * FROM customers WHERE customer_id = ?', (customer_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
