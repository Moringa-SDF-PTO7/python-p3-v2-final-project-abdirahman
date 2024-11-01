
from . import CURSOR, CONN

class Customer:
    def __init__(self, customer_id=None, name="", contact_information=""):
        self.customer_id = customer_id
        self.name = name
        self.contact_information = contact_information

    @classmethod
    def create_table(cls):
      
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_information INTEGER
            )
        ''')
        CONN.commit()

    def save(self):
       
        CURSOR.execute('''
            INSERT INTO customers (name, contact_information)
            VALUES (?, ?)
        ''', (self.name, self.contact_information))
        CONN.commit()

    @classmethod
    def find_by_id(cls, customer_id):
      
        CURSOR.execute('SELECT * FROM customers WHERE customer_id = ?', (customer_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM customers")
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    def update(self):
        CURSOR.execute('''
            UPDATE customers SET name = ?, contact_information = ?
            WHERE customer_id = ?
        ''', (self.name, self.contact_information, self.customer_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM customers WHERE customer_id = ?', (self.customer_id,))
        CONN.commit()
