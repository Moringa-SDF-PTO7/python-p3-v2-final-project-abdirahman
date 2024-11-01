
from . import CURSOR, CONN

class Supplier:
    def __init__(self, supplier_id=None, name="", contact_information="", location=""):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_information = contact_information
        self.location = location

    @classmethod
    def create_table(cls):
        
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact_information INT,
                location VARCHARS
            )
        ''')
        CONN.commit()

    def save(self):
        
        CURSOR.execute('''
            INSERT INTO suppliers (name, contact_information, location)
            VALUES (?, ?, ?)
        ''', (self.name, self.contact_information, self.location))
        CONN.commit()

    @classmethod
    def find_by_id(cls, supplier_id):
        
        CURSOR.execute('SELECT * FROM suppliers WHERE supplier_id = ?', (supplier_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
       
        CURSOR.execute("SELECT * FROM suppliers")
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    def update(self):
        CURSOR.execute('''
            UPDATE suppliers SET name = ?, contact_information = ?, location = ?
            WHERE supplier_id = ?
        ''', (self.name, self.contact_information, self.location, self.supplier_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM suppliers WHERE supplier_id = ?', (self.supplier_id,))
        CONN.commit()
