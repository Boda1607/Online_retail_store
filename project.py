import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('online_retail_store.db')
c = conn.cursor()

# Create tables
c.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone_number TEXT
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    order_date TEXT,
    quantity INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
''')

#--------------------------------------------------------------------------------------------------------
# Insert data
c.executemany('''
INSERT INTO Products (name, category, price, stock) VALUES (?, ?, ?, ?)
''', [
    ('Laptop', 'Electronics', 800, 10),
    ('Mobile', 'Electronics', 1200, 20),
    ('Chair', 'Furniture', 450, 9)
])

c.executemany('''
INSERT INTO Customers (name, email, phone_number) VALUES (?, ?, ?)
''', [
    ('Ahmed', 'Ahmed@example.com', '123'),
    ('AbdElRahman', 'AbdElRahman@example.com', '567')
])

c.executemany('''
INSERT INTO Orders (customer_id, product_id, order_date, quantity) VALUES (?, ?, ?, ?)
''', [
    (1, 1, '2025-01-01', 2),
    (2, 3, '2025-01-02', 2),
    (1, 2, '2025-01-03', 3)
])
#--------------------------------------------------------------------------------------------------------
# Implementation Plan:


#Update Tables
c.execute('''
UPDATE Customers SET phone_number = '999' WHERE name = 'Ahmed';
''')



#Select with Multiple Conditions:
s = '''
SELECT * FROM Orders
WHERE quantity > 1 OR order_date BETWEEN '2025-01-01' AND '2025-01-02';
'''
orders_with_multaple_conditions = pd.read_sql(s, conn)
print("Orders with Multiple conditions:\n", orders_with_multaple_conditions)



#Multiple Joins
s = '''
SELECT Orders.order_id, Customers.name, Products.name, Orders.quantity, Orders.order_date
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
JOIN Products ON Orders.product_id = Products.product_id;
'''
order_details = pd.read_sql(s, conn)
print("\nOrder Details:\n", order_details)



#Subqueries:
s = '''
SELECT name FROM Customers
WHERE customer_id IN (
    SELECT customer_id FROM Orders
    GROUP BY customer_id
    ORDER BY COUNT(order_id) DESC
    LIMIT 1
);
'''
top_customer = pd.read_sql(s, conn)
print("\nTop Customer:\n", top_customer)

conn.commit()
#--------------------------------------------------------------------------------------------------------
# 1. Generate sales report by product or category
sales_report = '''
SELECT category, SUM(quantity * price) as total_sales
FROM Orders
JOIN Products ON Orders.product_id = Products.product_id
GROUP BY category;
'''

sales_report = pd.read_sql(sales_report, conn)
print("Sales Report by Category:\n", sales_report)

# 2. Identify customers who made repeat purchases
repeat_customers = '''
SELECT Customers.name, COUNT(Orders.order_id) as total_orders
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
GROUP BY Customers.customer_id
HAVING total_orders > 1;
'''

repeat_customers = pd.read_sql(repeat_customers, conn)
print("\nRepeat Customers:\n", repeat_customers)

# 3. Analyze stock levels to determine reordering requirements
stock_levels = '''
SELECT name, stock
FROM Products
WHERE stock < 10;
'''
low_stock = pd.read_sql(stock_levels, conn)
#--------------------------------------------------------------------------------------------------------
# Export data to CSV
sales_report.to_csv('sales_report.csv', index=False)
repeat_customers.to_csv('repeat_customers.csv', index=False)
low_stock.to_csv('low_stock.csv', index=False)


conn.close()


sales_report_df = pd.read_csv('sales_report.csv')

# Display the first few rows of the DataFrame
print(sales_report_df.head())

