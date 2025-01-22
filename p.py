import pandas as pd


sales_report_df = pd.read_csv('sales_report.csv')
repeat_customers_df = pd.read_csv('repeat_customers.csv')
low_stock_df = pd.read_csv('low_stock.csv')


print("Sales Report:\n", sales_report_df.head())
print("\nRepeat Customers:\n", repeat_customers_df.head())
print("\nLow Stock Products:\n", low_stock_df.head())
