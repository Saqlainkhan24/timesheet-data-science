import pandas as pd
import numpy as np
from datetime import datetime
import calendar

# Step 1: Load project mapping file and process it
def load_project_mapping(file_path):
    # Load project mapping file
    df = pd.read_excel(file_path)
    
    # Drop first row and last two rows
    df = df.iloc[1:-2]
    
    # Fill 'to_date' and 'from_date' columns with forward fill
    df['To Date'].fillna(method='ffill', inplace=True)
    df['From Date'].fillna(method='ffill', inplace=True)
    
    # Drop 'planned_hours' column
    df.drop(columns=['Planned Hours'], inplace=True)
    
    # Apply formula ((x * 173) / 100) to 'planned_loading' column
    df['planned loading %'] = df['planned loading %'].astype(float)
    df['planned loading %'] = (df['planned loading %'] * 173) / 100
    
    return df

# Step 2: Load all timesheets and process each
def load_timesheets(timesheet_files):
    timesheet_dict = {}
    
    for file in timesheet_files:
        # Load timesheet
        ts = pd.read_excel(file)
        
        df = pd.read_excel(timesheet_files, header=None)
        
        # Drop the first row and last two rows using iloc
        df = df.iloc[1:-2]
        
        # Optionally reset the header (this assumes the second row is the header after dropping the first row)
        df.columns = df.iloc[0]  # Set the new header
        df = df[1:]  # Drop the new header row from the data
        
        # Construct the output file path
        
        # Save the modified DataFrame to a new Excel file
        df.to_excel(index=False, header=True)
        # Drop specified columns
        ts.drop(columns=['Status', 'Comments', 'Requester Remarks', 'Approver Remarks', 'Charge Code', 'Category'], inplace=True)
        
        # Convert 'hours' column to hh.mm format
        ts['Hours'] = ts['Hours'].apply(lambda x: int(x) + (x % 1) * 100 / 60)
        
        # Group data by 'employee_name' and 'project_name', then sum 'hours'
        ts_grouped = ts.groupby(['Employee Name', 'Project Name'], as_index=False)['Hours'].sum()
        
        # Sort values by 'project_name' and reset index
        ts_grouped = ts_grouped.sort_values(by='Project Name').reset_index(drop=True)
        
        # Merge timesheet with processed project mapping
        date_key = file.split('_')[-1].replace('.xlsx', '')  # Assuming date is part of the filename
        ts_merged = pd.merge(ts_grouped, project_mapping, on='Project Name', how='left')
        
        # Store in dictionary with date as key
        timesheet_dict[date_key] = ts_merged
    
    # Combine all timesheets into a single dataframe
    combined_df = pd.concat(timesheet_dict.values(), ignore_index=True)
    
    return combined_df

# Step 3: Filter combined dataframe and process dates
def filter_combined_dataframe(combined_df):
    # Convert 'to_date', 'from_date', and 'date' columns to mm-yy format and store in separate columns
    combined_df['to'] = pd.to_datetime(combined_df['To Date']).dt.strftime('%m-%y')
    combined_df['from'] = pd.to_datetime(combined_df['From Date']).dt.strftime('%m-%y')
    combined_df['date'] = pd.to_datetime(combined_df['Date']).dt.strftime('%m-%y')
    
    # Apply condition (date >= from & date <= to)
    filtered_df = combined_df[(combined_df['date'] >= combined_df['from']) & (combined_df['date'] <= combined_df['to'])]
    
    # Function to calculate number of days in each month between from_date and to_date
    def calculate_days(From_date, to_date):
        from_date = pd.to_datetime(from_date)
        to_date = pd.to_datetime(to_date)
        total_days = (to_date - from_date).days + 1
        return total_days
    
    filtered_df['days'] = filtered_df.apply(lambda x: calculate_days(x['From Date'], x['To Date']), axis=1)
    
    # Function to calculate actual total number of days in a month
    def days_in_month(date):
        date = pd.to_datetime(date, format='%Y-%m-%d')
        return calendar.monthrange(date.year, date.month)[1]
    
    filtered_df['days_of_month'] = filtered_df['date'].apply(lambda x: days_in_month(x))
    
    # Function to calculate total planned loading
    def calculate_planned_loading(pl, days, total_days_in_month):
        return (pl * days) / total_days_in_month
    
    filtered_df['planned loading %'] = filtered_df.apply(
        lambda x: calculate_planned_loading(x['planned_loading'], x['days'], x['days_of_month']), axis=1)
    
    return filtered_df

# Step 4: Convert filtered data into Excel file
def export_to_excel(filtered_df, output_file):
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        filtered_df.to_excel(writer, index=False)

# Main script execution
project_mapping_file = r'rptempproj (4) (1).xlsx'
timesheet_files = [
     r'c:\Users\Admin\Desktop\excel\0102024-rptdailytsemp (3).xlsx', r'c:\Users\Admin\Desktop\excel\0202024-rptdailytsemp.xlsx',
    r'c:\Users\Admin\Desktop\excel\0302024-rptdailytsemp.xlsx', r'c:\Users\Admin\Desktop\excel\0402024-rptdailytsemp.xlsx',
    r'c:\Users\Admin\Desktop\excel\0502024-rptdailytsemp.xlsx', r'c:\Users\Admin\Desktop\excel\0602024-rptdailytsemp.xlsx' ,
    r'c:\Users\Admin\Desktop\excel\0702024-rptdailytsemp.xlsx', r'c:\Users\Admin\Desktop\excel\0802024-rptdailytsemp.xlsx'
]  # Add your timesheet files here

# Load and process project mapping
project_mapping = load_project_mapping(project_mapping_file)

# Load and process all timesheets
combined_timesheets = load_timesheets(timesheet_files)

# Filter combined dataframe and apply necessary calculations
filtered_data = filter_combined_dataframe(combined_timesheets)

# Export the final filtered data to an Excel file
export_to_excel(filtered_data, 'output.xlsx')