
from . import CURSOR, CONN

class Product:
    def __init__(self, product_id=None, name="", price=0.0, quantity=0, supplier_id=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

    @classmethod
    def create_table(cls):
       
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
            )
        ''')
        CONN.commit()

    def save(self):
       
        CURSOR.execute('''
            INSERT INTO products (name, price, quantity, supplier_id)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.price, self.quantity, self.supplier_id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, product_id):
       
        CURSOR.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
       
        CURSOR.execute("SELECT * FROM products")
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    def update(self):
        CURSOR.execute('''
            UPDATE products SET name = ?, price = ?, quantity = ?, supplier_id = ?
            WHERE product_id = ?
        ''', (self.name, self.price, self.quantity, self.supplier_id, self.product_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM products WHERE product_id = ?', (self.product_id,))
        CONN.commit()
