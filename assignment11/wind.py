import plotly.express as px
import plotly.data as pldata
import webbrowser
import os

# 1. Load Plotly wind dataset
df = pldata.wind(return_type='pandas')

# Print first and last 10 rows
print("--- First 10 Rows ---")
print(df.head(10))
print("\n--- Last 10 Rows ---")
print(df.tail(10))

# 2. Clean 'strength' column (extract numeric values)
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
html_filename = "wind.html"
fig.write_html(html_filename)
print(f"\nSaved interactive plot to {html_filename} successfully!")

# 5. Load and verify the HTML file (Required by Task 3)
if os.path.exists(html_filename):
    with open(html_filename, 'r', encoding='utf-8') as f:
        html_content = f.read()
    print(f"Verified: {html_filename} successfully read ({len(html_content)} bytes).")
    
    # Automatically open in browser for interactive verification
    webbrowser.open('file://' + os.path.realpath(html_filename))