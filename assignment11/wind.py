import plotly.express as px
import plotly.data as pldata

# Load dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 lines
print("--- First 10 Rows ---")
print(df.head(10))
print("\n--- Last 10 Rows ---")
print(df.tail(10))

# Clean 'strength' column: extract the first numeric value (e.g. '0-1' -> 0.0, '6+' -> 6.0)
df['strength'] = df['strength'].astype(str).str.split('-').str[0].str.replace('+', '', regex=False).astype(float)

# Create interactive scatter plot
fig = px.scatter(
    df, 
    x='strength', 
    y='frequency', 
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

# Save to wind.html
fig.write_html('wind.html')
print("\nSaved plot successfully to wind.html")