
import os
import pandas as pd

# Define the folder containing the Excel files
file_path = r'0102024-rptdailytsemp.xlsx' ,r'0202024-rptdailytsemp.xlsx' ,r'0302024-rptdailytsemp.xlsx' , r'0402024-rptdailytsemp.xlsx' ,
r'0502024-rptdailytsemp.xlsx' ,r'0602024-rptdailytsemp.xlsx' ,r'0702024-rptdailytsemp.xlsx' ,r'0802024-rptdailytsemp.xlsx'
# List all Excel files in the folder


# Define the columns you want to extract
columns_to_extract = ['Employee Name', 'Project Name', 'Date', 'Hours','Employee Timesheet Details From 01/02/2024 To 29/02/2024',
                      'Employee Timesheet Details From 01/03/2024 To 31/03/2024','Employee Timesheet Details From 01/04/2024 To 30/04/2024',
                      'Employee Timesheet Details From 01/05/2024 To 31/05/2024','Employee Timesheet Details From 01/06/2024 To 30/06/2024',
                      'Employee Timesheet Details From 01/07/2024 To 31/07/2024','Employee Timesheet Details From 01/08/2024 To 31/08/2024']  # Replace with the correct columns

# Initialize a list to store the data from all files
all_data = []

# Loop through each file and extract the columns
for file in file_path:
    file_path = os.path.join(file_path, file)
    
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Print the columns in the current file for debugging
        print(f"Columns in {file}: {df.columns.tolist()}")
        
        
        
        
        # Extract the specific columns
        extracted_data = df[columns_to_extract]
        
        # Append the extracted data to the list
        all_data.append(extracted_data)
    
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Combine all extracted data into a single DataFrame if any data was extracted
if all_data:
    combined_data = pd.concat(all_data, ignore_index=True)
    
    # Save the combined data to a new Excel file
    output_file = "combined_data.xlsx"
    combined_data.to_excel(output_file, index=False)
    print(f"Data extracted and saved to {output_file}")

