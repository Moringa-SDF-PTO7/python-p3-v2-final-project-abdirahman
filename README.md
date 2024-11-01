# Phase 3 CLI+ORM Project Template

# Supplier Management System

## Overview

The Supplier Management System is a command-line interface (CLI) tool designed to manage suppliers, products, customers, orders, and order details. This project is implemented using an Object-Relational Mapping (ORM) approach to handle database interactions and follows a modular design for easy extension and maintenance. The system allows users to perform CRUD (Create, Read, Update, Delete) operations on all entities and ensures data consistency with foreign keys and validation checks.

## Directory Structure
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── supplier.py
    │   ├── product.py
    │   ├── customer.py
    │   ├── order.py
    │   └── order_detail.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Setting up the Environment

## Cloning the repository

git clone git@github.com:Moringa-SDF-PTO7/python-p3-v2-final-project-abdirahman.git

cd python-p3-v2-final-project-abdirahman

This project uses `pipenv` for managing dependencies. To set up the environment, run the following commands:

```console
pipenv install
pipenv shell


---

## CLI Structure and Description

The main CLI script is located in `lib/cli.py`. This script provides an interactive menu that allows users to manage suppliers, products, customers, orders, and order details. 

### Sample CLI Menu

When you run `python lib/cli.py`, the following options will be displayed:

- 1. Add a new supplier
- 2. View all products
- 3. Update customer information
- 4. Delete an order
- 5. Exit

The user can select options by entering the corresponding number. Each option directs to functions implemented in the `helpers.py` file, providing feedback and performing actions based on user input.

To exit the program, the user can choose the 'Exit' option from the main menu.

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

## Data Models and ORM

The data models are located in the `lib/models` folder. Each model represents a table in the database:

- **Supplier**: `ID` (Primary Key), `Name`, `Contact`
- **Product**: `Product_ID` (Primary Key), `Name`, `Price`, `Quantity`, `Supplier_ID` (Foreign Key)
- **Customer**: `Customer_ID` (Primary Key), `Name`, `Contact`
- **Order**: `Order_ID` (Primary Key), `Order_Date`, `Customer_ID` (Foreign Key)
- **Order Detail**: `Detail_ID` (Primary Key), `Order_ID` (Foreign Key), `Product_ID` (Foreign Key), `Quantity`

### Object-Relational Mapping (ORM)

This project uses a custom ORM implementation to map Python objects to database records. Each model has methods for create, read, update, and delete (CRUD) operations, which allow seamless interaction with the SQLite database. The ORM enforces foreign key relationships to maintain data integrity.

## LICENSE
This project is licensed under the MIT License. See the LICENSE file for more details.