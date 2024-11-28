
import pandas as pd

# List of Excel files to concatenate
excel_files = ['outputs1_file.xlsx','outputs2_file.xlsx','outputs3_file.xlsx' ,'outputs4_file.xlsx' ,'outputs5_file.xlsx' ,'outputs6_file.xlsx', 'outputs7_file.xlsx', 'outputs8_file.xlsx']

# Read each file into a DataFrame and store in a list
df_list = [pd.read_excel(file) for file in excel_files]

# Concatenate all DataFrames into one
concat_df = pd.concat(df_list, ignore_index=True)

# Save the concatenated DataFrame to a new Excel file
concat_df.to_excel('concatenated2_output.xlsx', index=False)

