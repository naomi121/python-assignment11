import plotly.data as pldata
import plotly.express as px

# 1. Load wind dataset using specified import
df = pldata.wind(return_type='pandas')

# 2. Print first 10 and last 10 rows
print("--- First 10 Rows ---")
print(df.head(10))

print("\n--- Last 10 Rows ---")
print(df.tail(10))

# 3. Define and apply clean_strength helper function
def clean_strength(val):
    if isinstance(val, str):
        val = val.replace('+', '')
        if '-' in val:
            parts = val.split('-')
            return (float(parts[0]) + float(parts[1])) / 2
    return float(val)

# Explicitly apply cleaning function to strength column
df['strength'] = df['strength'].apply(clean_strength)

# 4. Create scatter plot with strength vs frequency
fig = px.scatter(
    df,
    x="frequency",
    y="strength",
    color="direction",
    title="Wind Dataset: Frequency vs Strength by Direction",
    labels={"frequency": "Frequency", "strength": "Strength"}
)

# 5. Save HTML file
fig.write_html("wind.html")

# 6. Load and verify saved wind.html file
with open("wind.html", "r", encoding="utf-8") as f:
    html_content = f.read()

print(f"\nVerification: wind.html successfully loaded ({len(html_content)} characters read).")

