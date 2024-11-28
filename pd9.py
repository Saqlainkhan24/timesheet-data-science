import pandas as pd
from calendar import monthrange

def days_of_month(date):
    # Ensure date is a pandas Timestamp object
    if not isinstance(date, pd.Timestamp):
        raise ValueError("Date must be a pandas Timestamp object")
    
    # Get the number of days in the month for the given date
    _, num_days = monthrange(date.year, date.month)
    return num_days
# Load the Excel file
file_path = 'output12.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Convert the 'Date' column from 'mm-yy' format to datetime objects
df['Date'] = pd.to_datetime(df['Date'], format='%m-%y')

# Calculate the number of days in the month for each date
df['Days of Month'] = df['Date'].apply(days_of_month)

# Save the modified DataFrame to a new Excel file (optional)
df.to_excel('output13.xlsx', index=False)

print(df)
