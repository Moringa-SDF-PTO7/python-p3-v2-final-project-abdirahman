# lib/models/product.py
from . import CURSOR, CONN

class Product:
    def __init__(self, product_id, name, price, quantity, supplier_id):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier_id = supplier_id

    @classmethod
    def create_table(cls):
        """Create the products table if it doesn't exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL,
                quantity INTEGER,
                supplier_id INTEGER,
                FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
            )
        ''')
        CONN.commit()

    def save(self):
        """Save a new product to the database."""
        CURSOR.execute('''
            INSERT INTO products (name, price, quantity, supplier_id)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.price, self.quantity, self.supplier_id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, product_id):
        """Find a product by ID."""
        CURSOR.execute('SELECT * FROM products WHERE product_id = ?', (product_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
    
    @classmethod
    def all(cls):
        """Fetch all products from the database."""
        CURSOR.execute("SELECT * FROM products")
        rows = CURSOR.fetchall()
        products = [cls(*row) for row in rows]
        return products

