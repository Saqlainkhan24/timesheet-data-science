import pandas as pd

file_path = r'concatenated3_output.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Display the contents
# df.groupby("Employee Name").count()
'''df["Hours"]= pd.to_timedelta(df['Hours'],errors='coerce')

total_working_hr=df.groupby('Employee Name')['Hours'].sum().reset_index()

print(total_working_hr)'''

'''df['Date'] = pd.to_datetime(df['Date'])

# Extract the year and month from the 'Date' column to create a 'Month' column
df['Month'] = df['Date'].dt.to_period('M')

# Group by 'Month' and sum the 'Hours' for each month
monthly_totals = df.groupby['Employee Name']('Month')['Hours'].sum().reset_index()

# Rename columns for clarity
monthly_totals.columns = ['Employee Name','Month', 'Total_Hours']

# Print the result
print(monthly_totals)
'''

''' Convert Date column to datetime
df['file_path'] = pd.to_datetime(df['Date'])

# Extract year and month for grouping
df['Year-Month'] = df['file_path'].dt.to_period('M')

# Group by Name and Year-Month and sum the Hours
monthly_timesheet = df.groupby(['Employee Name', 'Year-Month'])['Hours'].sum().reset_index()

# Display the result
print(monthly_timesheet)'''


 # Remove extra spaces from column names

'''df = pd.read_excel('0202024-rptdailytsemp.xlsx', header=1)

df.columns = ['Employee', 'Date', 'Start Time', 'End Time', 'Hours', ...]

print(df.head())
'''


#Convert the Hours column from string format to timedelta
df['Hours'] = pd.to_timedelta(df['Hours'] + ':00')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

#Convert Date column to datetime
df['Year-Month'] = df['Date'].dt.to_period('M')


# Group by Name and Year-Month and sum the Hours (as timedelta)
monthly_timesheet = df.groupby(['Employee Name','Year-Month','Project Name'])['Hours'].sum().reset_index()

# Convert the timedelta back to a string format (hours:minutes)
monthly_timesheet['Total Hours'] = monthly_timesheet['Hours'].apply(lambda x: f"{int(x.total_seconds() // 3600)}:{int((x.total_seconds() % 3600) // 60):02d}")

# Drop the timedelta column if not needed
monthly_timesheet = monthly_timesheet.drop(columns=['Hours'])

# Display the result
print(monthly_timesheet)

#pd.set_option('display.max.rows',123)
#monthly_timesheet.to_excel('outputs8_file.xlsx', index=False)

