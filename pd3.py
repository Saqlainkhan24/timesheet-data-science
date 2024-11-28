
import pandas as pd

# Read only the required columns, e.g., 'Employee Name' and 'Total Hours'
df = pd.read_excel(r'c:\Users\Admin\Desktop\$rptempproj (4) (1).xlsx', usecols=['Employee Name','Project Name','From Date', 'To Date','Planned Hours'])
df.to_excel('extracted_columns1.xlsx', index=False)

print("Extracted columns saved to 'extracted_columns1.xlsx'.")
# Display the extracted columns
print(df)

