import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("../db/lesson.db")

# Query revenue by employee
query = """
SELECT e.last_name, SUM(p.price * l.quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

df = pd.read_sql_query(query, conn)
conn.close()

# Plot revenue bar chart
plt.figure(figsize=(8, 5))
plt.bar(df['last_name'], df['revenue'], color='skyblue')
plt.title('Total Revenue by Employee')
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()