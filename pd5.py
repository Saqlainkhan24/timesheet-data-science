import pandas as pd
import openpyxl
# Load the CSV file

df = pd.read_excel( r'c:\Users\Admin\Desktop\excel\0802024-rptdailytsemp.xlsx', header=None,)



# Check the existing header row
print(df.columns)

# Remove the header row
df = df.iloc[1:-2]

# Reset the index of the dataframe
df = df.reset_index(drop=True)

# Check the updated dataframe
print(df.head())

output_file = "output10_file.xlsx"

# Save the DataFrame to the Excel file
df.to_excel(output_file, header=False, index=False)

