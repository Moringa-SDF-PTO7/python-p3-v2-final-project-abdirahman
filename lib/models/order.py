# lib/models/order.py

from . import CURSOR, CONN

class Order:
    def __init__(self, order_id=None, order_date="", customer_id=None):
        self.order_id = order_id
        self.order_date = order_date
        self.customer_id = customer_id

    @classmethod
    def create_table(cls):
        """Create the orders table if it doesn't exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                order_date TEXT NOT NULL,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        ''')
        CONN.commit()

    def save(self):
        """Save a new order to the database."""
        CURSOR.execute('''
            INSERT INTO orders (order_date, customer_id)
            VALUES (?, ?)
        ''', (self.order_date, self.customer_id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, order_id):
        """Find an order by ID."""
        CURSOR.execute('SELECT * FROM orders WHERE order_id = ?', (order_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
        """Fetch all orders from the database."""
        CURSOR.execute("SELECT * FROM orders")
        rows = CURSOR.fetchall()
        orders = [cls(*row) for row in rows]
        return orders
