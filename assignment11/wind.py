import os
import pandas as pd
import plotly.express as px

# 1. Load the dataset (handles db directory or local paths automatically)
if os.path.exists("db/wind.csv"):
    df = pd.read_csv("db/wind.csv")
elif os.path.exists("db") and os.path.isfile("db"):
    df = pd.read_csv("db")
elif os.path.exists("assignment11/wind.csv"):
    df = pd.read_csv("assignment11/wind.csv")
else:
    df = pd.read_csv("wind.csv")

# 2. Print first and last 10 rows as required
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# 3. Clean strength column using .str.replace()
df['strength'] = df['strength'].astype(str).str.replace('knots', '', regex=False)
df['strength'] = df['strength'].str.replace('knot', '', regex=False)
df['strength'] = pd.to_numeric(df['strength'], errors='coerce')

# 4. Create the Plotly scatter plot
fig = px.scatter(
    df, 
    x="direction", 
    y="strength", 
    title="Wind Direction vs Strength"
)

# 5. Save the interactive HTML file inside the assignment11 directory
fig.write_html("assignment11/wind.html")
print("wind.html successfully generated in assignment11/")
