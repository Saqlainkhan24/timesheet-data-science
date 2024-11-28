import pandas as pd
import os

excel_files = r'c:\Users\Admin\Desktop\excel\0202024-rptdailytsemp.xlsx'

for file in excel_files:
    # Read the Excel file
    df = pd.read_excel(file)
    
    # Drop unwanted columns (replace 'UnwantedColumn' with actual column names)
    df_cleaned = df.drop(columns=['Employee Timesheet Details From 01/02/2024 To 29/02/2024', 'UnwantedColumn2'], errors='ignore')
    
    # Remove rows with missing values (optional: 'any' or 'all')
    df_cleaned = df_cleaned.dropna(how='any')  # Use 'how="all"' to drop rows with all NaN values
    
    # Fill missing values (example: fill with 0 or mean)
    df_cleaned['SomeColumn'] = df_cleaned['SomeColumn'].fillna(0)  # Or use df_cleaned.mean() to fill with the mean
    
    # Remove duplicates
    df_cleaned = df_cleaned.drop_duplicates()
    
    # Strip leading/trailing whitespace from string columns
    df_cleaned = df_cleaned.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Change data type of a column (example: convert to integer)
    df_cleaned['NumericColumn'] = df_cleaned['NumericColumn'].astype(int)
    
    # Save the cleaned data to a new Excel file (optional)
    output_file = f'cleaned_{file}'
    df_cleaned.to_excel(output_file, index=False)
    
    print(f'Cleaned data saved to {output_file}')
