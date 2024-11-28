import pandas as pd
from datetime import datetime
import calendar

# Load the Excel file
file_path = 'output11.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

def days_in_months(from_date, to_date):
    # Ensure both dates are datetime objects
    if not isinstance(from_date, pd.Timestamp) or not isinstance(to_date, pd.Timestamp):
        raise ValueError("Both from_date and to_date must be pandas Timestamp objects")

    total_days = 0
    current_date = from_date.replace(day=1)  # Start at the beginning of the month

    while current_date <= to_date:
        next_month = (current_date.month % 12) + 1
        next_month_year = current_date.year if next_month > 1 else current_date.year + 1
        last_day_of_month = datetime(next_month_year, next_month, 1) - pd.Timedelta(days=1)
        
        if to_date < last_day_of_month:
            last_day_of_month = to_date
        
        total_days += (last_day_of_month - current_date + pd.Timedelta(days=1)).days
        
        current_date = last_day_of_month + pd.Timedelta(days=1)

    return total_days

# Convert 'To Date' and 'From Date' columns from 'mm-yy' format to datetime objects
df['To Date'] = pd.to_datetime(df['To Date'], format='%m-%y')
df['From Date'] = pd.to_datetime(df['From Date'], format='%m-%y')

# Convert 'Date' column from 'mm-yy' format to datetime object
df['Date'] = pd.to_datetime(df['Date'], format='%m-%y')

# Apply the condition: Date >= From Date and Date <= To Date
filtered_df = df[(df['Date'] >= df['From Date']) & (df['Date'] <= df['To Date'])]

# Calculate number of days in each month between 'From Date' and 'To Date'
filtered_df['Days'] = filtered_df.apply(lambda row: days_in_months(row['From Date'], row['To Date']), axis=1)

# Save the modified DataFrame to a new Excel file (optional)
filtered_df.to_excel('output12.xlsx', index=False)

print(filtered_df)
