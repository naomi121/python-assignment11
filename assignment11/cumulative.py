import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("../db/lesson.db")

# Query order totals
query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Calculate cumulative revenue
df['cumulative'] = df['total_price'].cumsum()

# Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(df['order_id'], df['cumulative'], color='green', linewidth=2)
plt.title('Cumulative Revenue Over Time')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.show()