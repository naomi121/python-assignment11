import pandas as pd
import plotly.express as px
import plotly.data as pldata

# 1. Load the built-in Plotly wind dataset
df = pldata.wind(return_type='pandas')

# 2. Print first and last 10 rows as required
print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

# 3. Clean strength column using str.replace() then convert to float
df['strength'] = df['strength'].astype(str).str.replace(r'\D+', '', regex=True)
df['strength'] = df['strength'].astype(float)

# 4. Create the interactive scatter plot: strength vs frequency, colored by direction
fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Strength vs Frequency by Direction"
)

# 5. Save the interactive HTML file inside the assignment11 directory
fig.write_html("assignment11/wind.html")
print("wind.html successfully generated in assignment11/")