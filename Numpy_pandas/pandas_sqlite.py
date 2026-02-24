import pandas as pd
import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("sales.db")

# Create a sample table (normally you'd already have data)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL,
    order_date TEXT
)
""")

# Insert sample data
cursor.executemany("""
INSERT INTO orders (customer, product, quantity, price, order_date)
VALUES (?, ?, ?, ?, ?)
""", [
    ("Alice", "Laptop", 1, 1200, "2026-01-10"),
    ("Bob", "Phone", 2, 800, "2026-01-12"),
    ("Alice", "Tablet", 1, 300, "2026-01-15"),
    ("Diana", "Laptop", 1, 1200, "2026-01-20"),
    ("Eve", "Headphones", 3, 150, "2026-01-22"),
    ("Bob", "Phone", 1, 800, "2026-01-25")
])
conn.commit()

# Load data into pandas DataFrame
df = pd.read_sql("SELECT * FROM orders", conn)

# Add revenue column
df["Revenue"] = df["quantity"] * df["price"]

# Group by customer
customer_revenue = df.groupby("customer")["Revenue"].sum()

# Top product by revenue
top_product = df.groupby("product")["Revenue"].sum().sort_values(ascending=False).head(1)

print("Orders DataFrame:\n", df)
print("\nRevenue per Customer:\n", customer_revenue)
print("\nTop Product by Revenue:\n", top_product)

# Close connection
conn.close()