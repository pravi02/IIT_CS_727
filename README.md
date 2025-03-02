# Inventory Management Application

This project is a Python-based inventory management application that
allows users to interact with a MySQL database through a web
interface. It allows users to perform various database queries using complex 
SQL operations such as set operations, subqueries with WITH clauses, 
advanced aggregates, and OLAP queries. The system also provides a 
user-friendly interface for CRUD operations, and features robust error handling 
to ensure smooth user experience.

## Table of Contents

-   [Features](#features)

-   [Supported Tables](#supported-tables)

-   [Setup Instructions](#setup-instructions)

-   [Usage](#usage)

-   [Error Handling](#error-handling)

-   [Code Structure](#code-structure)

-   [Example Output](#example-output)


## Features

- **Complex SQL Queries:**
  
  - **Set Operations:** Union, Intersect, Difference, Symmetric Difference.
  - **Subqueries with CTE:** Total fines, road accidents, user violations.
  - **Advanced Aggregate Queries:** Rollup, running totals, and averages.
  - **OLAP Queries:** Ranking, partitioning, and percentage contribution.

- **User-Friendly Interface**:

    - Intuitive navigation with dropdown menus and buttons.
    - Interactive query execution with real-time results display.

- **CRUD Operations**:

    - Create, View, Update, and Delete records in all tables
   
- **Error Handling**:
      
    - Provides meaningful error messages for invalid operations.
    - Ensures graceful degradation and prevents application crashes.

# **Technologies Used** 💻

- Backend: Flask (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: MySQL
- Other Tools:
  - Loom for demonstration video
  - Git for version control

# Installation 🛠️

Follow these steps to set up and run the project on your local machine:

## Prerequisites:

- Python 3.8 or above
- MySQL server


## Supported Tables

The application supports the following tables:

1.  customer

2.  customer_order

    1.  customer_order_items

3.  inventory

   1. inventory location

4.  product 
   1. product\_ category
   2. supplier

7.  order_process

    1.  processed_line_items

8.  User

These tables are managed using primary keys, and relationships between them are enforced by the application logic.

## Setup Instructions

### Prerequisites

-   Python 3.x installed on your system.

-   MySQL server running with a valid database schema.

-   MySQL Connector for Python (pymsql, sqlalchemy, python-dotenv
    package).

### Installation

1.  Clone or download this repository to your local machine.

2.  Install following packages if not already installed:
```bash
pip install django python-dotenv crispy-bootstrap5
```
3.  Update the database connection credentials in the .env file with the
    parameters below:
```bash
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_HOST=
DATABASE_PORT=
```
The database schema - the required tables and relationships will be created once you run migrations.

## Usage

1.  **Run the application**:
```bash
python manage.py runserver
 ```
2.  **Menu Options**:

-   The application will display a menu with five options:

    -   Dashboard

    -   Orders Home

    -   Inventory Home

    -   Product Home

    -   People Home

-   Choose appropriate menu item for next action.

3.  **CRUD Operations**:

-   Create: Select appropriate menu item and, then click create new button and provide the required fields. The
    application checks for constraints like foreign key relationships
    before insertion.

-   Read: Select appropriate menu item to read the table.

-   Update: click the edit button next to the row to update values.

-   Delete: click the delete button next to the record to delete the row.

4.  **Exit**:

-   To exit the application, select sign out from the top right user account drop down menu or just close the browser

## Error Handling

-   **Database Connection**: If the application fails to connect to the
    MySQL database, it displays an error message and exits gracefully.

-   **Constraint Violations**: The application enforces foreign key
    constraints. If a user tries to insert/delete a record in a referenced table, it displays an error message.

-   **Business Logic Validation**: The application enforces business
    logic while updating or deleting records (EX: if customer order
    already processed then it will not let you update or delete)
