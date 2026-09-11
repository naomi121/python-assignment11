import plotly.data as pldata
import plotly.express as px

# 1. Load wind dataset using pldata.wind(return_type='pandas')
df = pldata.wind(return_type='pandas')

# 2. Print first 10 and last 10 rows
print("--- First 10 Rows ---")
print(df.head(10))

print("\n--- Last 10 Rows ---")
print(df.tail(10))

# 3. Clean the strength column using .str.replace() and convert to float
# Strip '+' signs using pandas .str.replace()
df['strength'] = df['strength'].astype(str).str.replace('+', '', regex=False)

# Convert range strings (like '0-1') to average numeric floats
def parse_range(val):
    if '-' in val:
        parts = val.split('-')
        return (float(parts[0]) + float(parts[1])) / 2
    return float(val)

df['strength'] = df['strength'].apply(parse_range)

# 4. Create scatter plot with strength vs frequency
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Dataset: Frequency vs Strength by Direction",
    labels={"frequency": "Frequency", "strength": "Strength"}
)

# 5. Save interactive HTML file
fig.write_html("wind.html")

# 6. Verify HTML file can be read back in
with open("wind.html", "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"\nVerification: wind.html successfully loaded ({len(html_content)} characters read).")

