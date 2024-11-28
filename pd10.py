import pandas as pd
from calendar import monthrange

def calculate_total_planned_loading(pl, date, days):
    # Ensure 'pl' is a numeric value and 'date' is a pandas Timestamp object
    if not isinstance(date, pd.Timestamp):
        raise ValueError("Date must be a pandas Timestamp object")
    
    # Get the number of days in the month for the given date
    _, total_days_of_month = monthrange(date.year, date.month)
    
    # Calculate the total planned loading
    total_planned_loading = (pl * days) / total_days_of_month
    return total_planned_loading

# Load the Excel file
file_path = 'output13.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Convert the 'Date' column from 'mm-yy' format to datetime objects
df['Date'] = pd.to_datetime(df['Date'], format='%m-%y')

# Ensure 'Planned Loading %' and 'Days' columns are numeric
df['Planned Loading %'] = pd.to_numeric(df['Planned Loading %'], errors='coerce')
df['Days'] = pd.to_numeric(df['Days'], errors='coerce')

# Calculate the new 'Planned Loading %' based on the formula
df['Planned Loading %'] = df.apply(
    lambda row: calculate_total_planned_loading(row['Planned Loading %'], row['Date'], row['Days']),
    axis=1
)

# Save the modified DataFrame to a new Excel file (optional)
df.to_excel('output14.xlsx', index=False)

print(df)
