import pandas as pd

# Sample data

df = pd.read_excel(r'output_file.xlsx')


## Print column names to verify
print("to:", df.columns)

print("from:", df.columns)
# Convert columns to datetime
df['ToDate'] = pd.to_datetime(df['ToDate'])
df['FromDate'] = pd.to_datetime(df['FromDate'])
df['Date'] = pd.to_datetime(df['Date'])

# Format columns to mm-yy
df['To'] = df['ToDate'].dt.strftime('%m-%y')
df['From'] = df['FromDate'].dt.strftime('%m-%y')
df['Date'] = df['Date'].dt.strftime('%m-%y')

# Convert formatted columns back to datetime for comparison
df['To'] = pd.to_datetime(df['To'], format='%m-%y')
df['From'] = pd.to_datetime(df['From'], format='%m-%y')
df['Date'] = pd.to_datetime(df['Date'], format='%m-%y')

# Apply the condition
df_filtered = df[(df['Date'] >= df['From']) & (df['Date'] <= df['To'])]

print(df_filtered)
