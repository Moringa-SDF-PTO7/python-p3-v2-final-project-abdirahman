# lib/cli.py

from models.supplier import Supplier
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_detail import OrderDetail

from helpers import exit_program

def main():
    while True:
        menu()
        choice = input("> ")
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_suppliers()
        elif choice == "2":
            add_supplier()
        elif choice == "3":
            list_products()
        elif choice == "4":
            add_product()
        elif choice == "5":
            list_customers()
        elif choice == "6":
            add_customer()
        elif choice == "7":
            list_orders()
        elif choice == "8":
            add_order()
        elif choice == "9":
            list_order_details()
        elif choice == "10":
            add_order_details()
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")
def menu():
    print("Supplier Management System")
    print("0. Exit")
    print("1. List all suppliers")
    print("2. Add a new supplier")
    print("3. List all products")
    print("4. Add a new product")
    print("5. List all customers")
    print("6. Add a new customer")
    print("7. List all orders")
    print("8. Add a new order")
    print("9. List all order_details")
    print("10. Add order details")


def list_suppliers():
    """List all suppliers."""
    suppliers = Supplier.all()
    if suppliers:
        print("\nSuppliers:")
        for supplier in suppliers:
            print(f"ID: {supplier.supplier_id}, Name: {supplier.name}, Contact: {supplier.contact_information}, Location: {supplier.location}")
    else:
        print("No suppliers found.")


def add_supplier():
    name = input("Enter supplier name: ")
    contact_info = input("Enter contact information: ")
    location = input("Enter location: ")
    supplier = Supplier(None, name, contact_info, location)
    supplier.save()
    print("Supplier added successfully.")

def list_products():
    print("\nProducts:")
    products = Product.all()
    if products:
        for product in products:
            print(f"{product.product_id}: {product.name} - ${product.price:.2f} - Qty: {product.quantity} - Supplier ID: {product.supplier_id}")
    else:
        print("No products found.")


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    supplier_id = int(input("Enter supplier ID: "))
    product = Product(None, name, price, quantity, supplier_id)
    product.save()
    print("Product added successfully.")


def list_customers():
    """List all customers."""
    customers = Customer.all()
    if customers:
        print("\nCustomers:")
        for customer in customers:
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Contact: {customer.contact_information}")
    else:
        print("No customers found.")

def add_customer():
    name = input("Enter customer name: ")
    contact_info = input("Enter contact information: ")
    customer = Customer(None, name, contact_info)
    customer.save()
    print("Customer added successfully.")


def list_orders():
    """List all orders."""
    orders = Order.all()
    if orders:
        print("\nOrders:")
        for order in orders:
            print(f"Order ID: {order.order_id}, Date: {order.order_date}, Customer ID: {order.customer_id}")
    else:
        print("No orders found.")

def add_order():
    order_date = input("Enter order date (YYYY-MM-DD): ")
    customer_id = int(input("Enter customer ID: "))
    order = Order(None, order_date, customer_id)
    order.save()
    print("Order added successfully.")


def list_order_details():
    """List all order details."""
    order_details = OrderDetail.all()
    if order_details:
        print("\nOrder Details:")
        for detail in order_details:
            print(f"Order Detail ID: {detail.order_detail_id}, Order ID: {detail.order_id}, Product ID: {detail.product_id}, Quantity: {detail.quantity}")
    else:
        print("No order details found.")
def add_order_details():
    order_id = int(input("Enter order ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    order_detail = OrderDetail(None, order_id, product_id, quantity)
    order_detail.save()
    print("Order detail added successfully.")


if __name__ == "__main__":
    main()
