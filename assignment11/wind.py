import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print("--- First 10 Rows ---")
print(df.head(10))
print("\n--- Last 10 Rows ---")
print(df.tail(10))

if df['strength'].dtype == 'object':
    df['strength'] = df['strength'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['strength'] = df['strength'].astype(float)

fig = px.scatter(
    df, 
    x='strength', 
    y='frequency', 
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'}
)

fig.write_html('wind.html')
print("Saved plot to wind.html")
