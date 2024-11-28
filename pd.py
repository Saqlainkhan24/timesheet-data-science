import pandas as pd
import os

df = pd.read_excel = r'0102024-rptdailytsemp.xlsx'

# Convert the Hours column from string format to timedelta
df['Hours'] = pd.to_timedelta(df['Hours'] + ':00')


# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract year and month for grouping
df['Year-Month'] = df['Date'].dt.to_period('M')

# Group by Name and Year-Month and sum the Hours (as timedelta)
monthly_timesheet = df.groupby(['Name', 'Year-Month'])['Hours'].sum().reset_index()

# Convert the timedelta back to a string format (hours:minutes)
monthly_timesheet['Total Hours'] = monthly_timesheet['Hours'].apply(lambda x: f"{int(x.total_seconds() // 3600)}:{int((x.total_seconds() % 3600) // 60):02d}")

# Drop the timedelta column if not needed
monthly_timesheet = monthly_timesheet.drop(columns=['Hours'])

# Display the result
print(monthly_timesheet)

monthly_timesheet.to_excel('outputs1_file.xlsx', index=False)
