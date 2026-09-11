import pandas as pd
import plotly.express as px

# 1. Load the wind dataset from Plotly Express
df = px.data.wind()

# 2. Print the first 10 rows and last 10 rows
print("--- First 10 Rows ---")
print(df.head(10))

print("\n--- Last 10 Rows ---")
print(df.tail(10))

# 3. Clean the strength column (convert range strings like '0-1' to average numeric values)
def clean_strength(val):
    if isinstance(val, str):
        val = val.replace('+', '')
        if '-' in val:
            parts = val.split('-')
            return (float(parts[0]) + float(parts[1])) / 2
    return float(val)


# 4. Create an interactive scatter plot
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Dataset: Frequency vs Strength by Direction",
    labels={"frequency": "Frequency", "strength": "Strength"}
)

# 5. Save the interactive chart as HTML
fig.write_html("wind.html")
print("\nSuccess: wind.html created!")