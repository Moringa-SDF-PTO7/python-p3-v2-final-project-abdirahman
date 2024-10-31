# lib/models/order_detail.py
from . import CURSOR, CONN

class OrderDetail:
    def __init__(self, detail_id, order_id, product_id, quantity):
        self.detail_id = detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    @classmethod
    def create_table(cls):
        """Create the order_details table if it doesn't exist."""
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                detail_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        ''')
        CONN.commit()

    def save(self):
        """Save a new order detail to the database."""
        CURSOR.execute('''
            INSERT INTO order_details (order_id, product_id, quantity)
            VALUES (?, ?, ?)
        ''', (self.order_id, self.product_id, self.quantity))
        CONN.commit()

    @classmethod
    def find_by_id(cls, detail_id):
        """Find an order detail by ID."""
        CURSOR.execute('SELECT * FROM order_details WHERE detail_id = ?', (detail_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None
