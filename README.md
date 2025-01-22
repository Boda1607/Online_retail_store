# Online Retail Store Database Project

This project demonstrates the implementation of a simple online retail store database using Python, SQLite, and Pandas. It simulates the functionality of an e-commerce platform by managing products, customers, and orders.

## Project Structure

- **Database**: An SQLite database called `online_retail_store.db` that holds three primary tables: 
  - **Products**: Contains details about products (e.g., name, category, price, stock).
  - **Customers**: Stores customer information (e.g., name, email, phone number).
  - **Orders**: Keeps track of orders placed by customers, including order date and quantity.

- **Python Code**: Python code used to interact with the database. It includes functionality for:
  - Creating the database schema and tables.
  - Inserting sample data into the tables.
  - Running SQL queries to generate reports.
  - Manipulating data (adding/deleting columns, filtering, etc.).
  - Exporting data to CSV files.

- **CSV Files**: Three CSV files generated from the database:
  - `sales_report.csv`: Sales report by category.
  - `repeat_customers.csv`: List of customers who made repeat purchases.
  - `low_stock.csv`: Products with low stock.

## Features

- **Sales Report**: Generates a report summarizing total sales by product category.
- **Repeat Customers**: Identifies customers who made repeat purchases.
- **Low Stock Products**: Lists products with stock levels below a threshold (10 in this case).
- **Data Manipulation**: Uses Pandas for data manipulation, including adding new columns, deleting columns, and filtering rows.
- **Export to CSV**: The generated data is exported to CSV files for analysis or further use.

## Requirements

- Python 3.x
- Pandas
- SQLite (Python's built-in SQLite support is used)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/online_retail_store.git

 2. Install the required libraries:

   ```bash
   pip install pandas
