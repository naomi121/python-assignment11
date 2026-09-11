import plotly.express as px
import plotly.data as pldata

# 1. Load Plotly wind dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("--- First 10 Rows ---")
print(df.head(10))
print("\n--- Last 10 Rows ---")
print(df.tail(10))

# 2. Clean 'strength' column (convert string values to numeric floats)
df['strength'] = df['strength'].astype(str).str.extract(r'(\d+\.?\d*)').astype(float)

# 3. Create interactive scatter plot
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs. Frequency by Direction",
    labels={"strength": "Wind Strength", "frequency": "Frequency"}
)

# 4. Save plot as wind.html
fig.write_html("wind.html")
print("\nSaved interactive plot to wind.html successfully!")