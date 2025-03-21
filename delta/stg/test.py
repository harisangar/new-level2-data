import duckdb
import pandas
import json

# Connect to the DuckDB database
connection = duckdb.connect('duckdb.duckdb')

# Example query to fetch data
tables = connection.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'silver'
""").fetchall()

print(tables)
# customers_data = connection.execute("SELECT * FROM Silver.dim_customers").fetchdf()
# payments_data = connection.execute("SELECT * FROM Silver.dim_payments").fetchdf()
# sales_data = connection.execute("SELECT * FROM Silver.fact_sales").fetchdf()

# print("Customers Data:\n", customers_data)
# print("Payments Data:\n", payments_data)
# print("Sales Data:\n", sales_data)