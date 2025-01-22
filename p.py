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




c.execute('''
UPDATE Orders SET quantity = 5 WHERE order_id = 1;
''')

# Update customer phone number
c.execute('''
UPDATE Customers SET phone_number = '999' WHERE customer_id = 2;
''')
conn.close()




