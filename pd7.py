import pandas as pd
from datetime import datetime
import calendar
import pandas as pd


df = pd.read_excel(r'Saqlain9.xlsx')

# Step 2: Convert 'todate', 'fromdate', and 'date' columns to datetime format
df['To Date'] = pd.to_datetime(df['To Date'])
df['From Date'] = pd.to_datetime(df['From Date'])
#df['date'] = pd.to_datetime(df['date'])

# Step 3: Format 'todate' and 'fromdate' into 'mm-yy' format and store them in 'to' and 'from' columns
df['to'] = df['To Date'].dt.strftime('%m-%y')
df['from'] = df['From Date'].dt.strftime('%m-%y')

# Step 4: Optionally, check the resulting DataFrame
print(df[['From Date', 'To Date', 'to', 'from']].head())

# Step 5: (Optional) Save the DataFrame to Excel if needed
df.to_excel('Saqlain10.xlsx', index=False)
