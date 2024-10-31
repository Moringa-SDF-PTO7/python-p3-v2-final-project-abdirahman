# lib/models/__init__.py

import sqlite3

# database connection
CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

# Importing model classes
from .supplier import Supplier
from .product import Product
from .customer import Customer
from .order import Order
from .order_detail import OrderDetail

# creating tables
Supplier.create_table()
Product.create_table()
Customer.create_table()
Order.create_table()
OrderDetail.create_table()
