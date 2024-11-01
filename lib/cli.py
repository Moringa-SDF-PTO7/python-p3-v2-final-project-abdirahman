# lib/cli.py

from models.supplier import Supplier
from models.supplier import Supplier
from models.product import Product
from models.customer import Customer
from models.order import Order
from models.order_detail import OrderDetail

from helpers import exit_program

def main():
    while True:
        try:
            menu()
            choice = input("> ").strip()
            handle_choice(choice)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def handle_choice(choice):
    try:
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_suppliers()
        elif choice == "2":
            add_supplier()
        elif choice == "3":
            update_supplier()
        elif choice == "4":
            delete_supplier()
        elif choice == "5":
            list_products()
        elif choice == "6":
            add_product()
        elif choice == "7":
            update_product()
        elif choice == "8":
            delete_product()
        elif choice == "9":
            list_customers()
        elif choice == "10":
            add_customer()
        elif choice == "11":
            update_customer()
        elif choice == "12":
            delete_customer()
        elif choice == "13":
            list_orders()
        elif choice == "14":
            add_order()
        elif choice == "15":
            update_order()
        elif choice == "16":
            delete_order()
        elif choice == "17":
            list_order_details()
        elif choice == "18":
            add_order_details()
        elif choice == "19":
            update_order_details()
        elif choice == "20":
            delete_order_details()
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def safe_int_input(prompt):
    """Get an integer input from the user, with error handling for invalid input."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def menu():
    print("Supplier Management System")
    print("0. Exit")
    print("1. List all suppliers")
    print("2. Add a new supplier")
    print("3. Update a supplier")
    print("4. Delete a supplier")
    print("5. List all products")
    print("6. Add a new product")
    print("7. Update a product")
    print("8. Delete a product")
    print("9. List all customers")
    print("10. Add a new customer")
    print("11. Update a customer")
    print("12. Delete a customer")
    print("13. List all orders")
    print("14. Add a new order")
    print("15. Update an order")
    print("16. Delete an order")
    print("17. List all order details")
    print("18. Add order details")
    print("19. Update order details")
    print("20. Delete order details")

def list_suppliers():
    """List all suppliers."""
    try:
        suppliers = Supplier.all()
        if suppliers:
            print("\nSuppliers:")
            for supplier in suppliers:
                print(f"ID: {supplier.supplier_id}, Name: {supplier.name}, Contact: {supplier.contact_information}, Location: {supplier.location}")
        else:
            print("No suppliers found.")
    except Exception as e:
        print(f"Error retrieving suppliers: {e}")

def add_supplier():
    try:
        name = input("Enter supplier name: ")
        contact_info = safe_int_input("Enter numeric contact information: ")
        location = input("Enter location: ")
        supplier = Supplier(None, name, contact_info, location)
        supplier.save()
        print("Supplier added successfully.")
    except Exception as e:
        print(f"Error adding supplier: {e}")

def update_supplier():
    try:
        supplier_id = safe_int_input("Enter the ID of the supplier to update: ")
        supplier = Supplier.find_by_id(supplier_id)
        if supplier:
            supplier.name = input("New name (leave blank to keep current): ") or supplier.name
            contact_info = safe_int_input("Enter new numeric contact information: ")
            supplier.contact_information = contact_info
            supplier.location = input("New location (leave blank to keep current): ") or supplier.location
            supplier.update()
            print("Supplier updated successfully.")
        else:
            print("Supplier not found.")
    except Exception as e:
        print(f"Error updating supplier: {e}")

def delete_supplier():
    try:
        supplier_id = safe_int_input("Enter the ID of the supplier to delete: ")
        supplier = Supplier.find_by_id(supplier_id)
        if supplier:
            supplier.delete()
            print("Supplier deleted successfully.")
        else:
            print("Supplier not found.")
    except Exception as e:
        print(f"Error deleting supplier: {e}")


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

def update_product():
    product_id = int(input("Enter the ID of the product to update: "))
    product = Product.find_by_id(product_id)
    if product:
        product.name = input("Enter new product name: ") or product.name
        product.price = float(input("Enter new price: ") or product.price)
        product.quantity = int(input("Enter new quantity: ") or product.quantity)
        product.supplier_id = int(input("Enter new supplier ID: ") or product.supplier_id)
        product.update()
        print("Product updated successfully.")
    else:
        print("Product not found.")

def delete_product():
    product_id = int(input("Enter the ID of the product to delete: "))
    product = Product.find_by_id(product_id)
    if product:
        product.delete()
        print("Product deleted successfully.")
    else:
        print("Product not found.")


def list_customers():
    """List all customers."""
    try:
        customers = Customer.all()
        if customers:
            print("\nCustomers:")
            for customer in customers:
                print(f"ID: {customer.customer_id}, Name: {customer.name}, Contact: {customer.contact_information}")
        else:
            print("No customers found.")
    except Exception as e:
        print(f"Error retrieving customers: {e}")

def add_customer():
    try:
        name = input("Enter customer name: ")
        contact_info = safe_int_input("Enter numeric contact information: ")
        customer = Customer(None, name, contact_info)
        customer.save()
        print("Customer added successfully.")
    except Exception as e:
        print(f"Error adding customer: {e}")

def update_customer():
    try:
        customer_id = safe_int_input("Enter the ID of the customer to update: ")
        customer = Customer.find_by_id(customer_id)
        if customer:
            customer.name = input("Enter new customer name (leave blank to keep current): ") or customer.name
            contact_info = safe_int_input("Enter new numeric contact information: ")
            customer.contact_information = contact_info
            customer.update()
            print("Customer updated successfully.")
        else:
            print("Customer not found.")
    except Exception as e:
        print(f"Error updating customer: {e}")

def delete_customer():
    try:
        customer_id = safe_int_input("Enter the ID of the customer to delete: ")
        customer = Customer.find_by_id(customer_id)
        if customer:
            customer.delete()
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")
    except Exception as e:
        print(f"Error deleting customer: {e}")


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

def update_order():
    order_id = int(input("Enter the ID of the order to update: "))
    order = Order.find_by_id(order_id)
    if order:
        order.order_date = input("Enter new order date (YYYY-MM-DD): ") or order.order_date
        order.customer_id = int(input("Enter new customer ID: ") or order.customer_id)
        order.update()
        print("Order updated successfully.")
    else:
        print("Order not found.")

def delete_order():
    order_id = int(input("Enter the ID of the order to delete: "))
    order = Order.find_by_id(order_id)
    if order:
        order.delete()
        print("Order deleted successfully.")
    else:
        print("Order not found.")


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

def update_order_details():
    detail_id = int(input("Enter the ID of the order detail to update: "))
    order_detail = OrderDetail.find_by_id(detail_id)
    if order_detail:
        order_detail.order_id = int(input("Enter new order ID: ") or order_detail.order_id)
        order_detail.product_id = int(input("Enter new product ID: ") or order_detail.product_id)
        order_detail.quantity = int(input("Enter new quantity: ") or order_detail.quantity)
        order_detail.update()
        print("Order detail updated successfully.")
    else:
        print("Order detail not found.")

def delete_order_details():
    detail_id = int(input("Enter the ID of the order detail to delete: "))
    order_detail = OrderDetail.find_by_id(detail_id)
    if order_detail:
        order_detail.delete()
        print("Order detail deleted successfully.")
    else:
        print("Order detail not found.")

if __name__ == "__main__":
    main()
