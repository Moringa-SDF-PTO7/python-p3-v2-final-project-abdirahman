
from . import CURSOR, CONN

class OrderDetail:
    def __init__(self, order_detail_id=None, order_id=None, product_id=None, quantity=0):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    @classmethod
    def create_table(cls):
       
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES orders(order_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id)
            )
        ''')
        CONN.commit()

    def save(self):
       
        CURSOR.execute('''
            INSERT INTO order_details (order_id, product_id, quantity)
            VALUES (?, ?, ?)
        ''', (self.order_id, self.product_id, self.quantity))
        CONN.commit()

    @classmethod
    def find_by_id(cls, order_detail_id):
        CURSOR.execute('SELECT * FROM order_details WHERE order_detail_id = ?', (order_detail_id,))
        row = CURSOR.fetchone()
        return cls(*row) if row else None

    @classmethod
    def all(cls):
        CURSOR.execute("SELECT * FROM order_details")
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    def update(self):
        CURSOR.execute('''
            UPDATE order_details SET order_id = ?, product_id = ?, quantity = ?
            WHERE order_detail_id = ?
        ''', (self.order_id, self.product_id, self.quantity, self.order_detail_id))
        CONN.commit()

    def delete(self):
        CURSOR.execute('DELETE FROM order_details WHERE order_detail_id = ?', (self.order_detail_id,))
        CONN.commit()
