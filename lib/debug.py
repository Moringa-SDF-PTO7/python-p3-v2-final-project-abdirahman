#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.supplier import Supplier
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_detail import OrderDetail
import ipdb

# Optional: Create sample data for testing
def setup_sample_data():
    # Create sample suppliers
    supplier1 = Supplier("ABC Supplies", "123-456-7890", "123 Market Street")
    supplier1.save()

    supplier2 = Supplier("XYZ Corp", "987-654-3210", "456 Business Blvd")
    supplier2.save()

    # Create sample products
    product1 = Product("Widget", 19.99, supplier1.supplier_id)
    product1.save()

    product2 = Product("Gadget", 29.99, supplier2.supplier_id)
    product2.save()

# Call function to setup sample data if needed
setup_sample_data()

# Enter the debugging session
ipdb.set_trace()
