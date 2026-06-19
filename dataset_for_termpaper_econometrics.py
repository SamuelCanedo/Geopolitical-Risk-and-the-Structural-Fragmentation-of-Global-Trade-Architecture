# dataset_for_termpaper_econometrics.py
# Samuel Canedo - Intemediate Econometrics - Term Paper

import os
import pandas as pd

# We get the location of the data
script_dir = os.path.dirname(__file__)  
file_path = os.path.join(script_dir, 'data_gpr.xls')

# Load the file safely
df = pd.read_excel(file_path)

## We check the data
print(df.head())

# Extract the year from the month column
df['year'] = pd.to_datetime(df['month']).dt.year

# Select the country columns 
prefix = 'GPRC_'
country_columns = [col for col in df.columns if col.startswith(prefix)]

# Keep the year and the country columns, then average
df_filtered = df[['year'] + country_columns]
df_annual = df_filtered.groupby('year').mean().reset_index()

# Reshape form wide format to long format 
df_long = pd.melt(
    df_annual, 
    id_vars=['year'], 
    value_vars=country_columns, 
    var_name='country_code', 
    value_name='gpr'
)

# Clean the country codes so 'GPRC_' is removed
df_long['country_code'] = df_long['country_code'].str.replace(prefix, '')

# Take out Taiwan since we don't have control variables for it
df_long = df_long[df_long['country_code'] != 'TWN']

# Save
df_long.to_csv(os.path.join(script_dir, 'gpr_annual.csv'), index=False)

print(f"Dataset generado. Países únicos incluidos: {len(df_long['country_code'].unique())}")

############ Control variables ############
import numpy as np

df_wb = pd.read_csv(os.path.join(script_dir, 'control_variables.csv'))

# Replace the missing values on the df
df_wb = df_wb.replace('..', np.nan)

# Identify the year columns 
years_cols = [col for col in df_wb.columns if '[YR' in col]

# Pass the years of the columns to lines
df_long_wb = pd.melt(
    df_wb, 
    id_vars=['Country Name', 'Country Code', 'Series Name'], 
    value_vars=years_cols, 
    var_name='year_raw', 
    value_name='value'
)

# Clean the year to be a single number
df_long_wb['year'] = df_long_wb['year_raw'].str.split(' ').str[0].astype(int)

# Standarized the names of the variables before pivot
def clean_series_name(name):
    if pd.isna(name) or not isinstance(name, str):
        return str(name)  # Return as is if it's NaN or not a string
    

    if 'Trade' in name:
        return 'trade'
    elif 'GDP growth' in name:
        return 'gdp_growth'
    elif 'Inflation' in name:
        return 'inflation'
    return name

df_long_wb['Series Name'] = df_long_wb['Series Name'].apply(clean_series_name)

# Pivot the data to have one row per country-year and columns for each variable
df_controls = df_long_wb.pivot_table(
    index=['Country Code', 'year'], 
    columns='Series Name', 
    values='value',
    aggfunc='first'
).reset_index()

# Rename the column of the code of country 
df_controls = df_controls.rename(columns={'Country Code': 'country_code'})

# Save the dataset of the control variables
df_controls.to_csv(os.path.join(script_dir, 'control_variables_long.csv'), index=False)

print(df_controls.head())

################## Merge the datasets ##################
df_gpr = pd.read_csv(os.path.join(script_dir, 'gpr_annual.csv'))
df_controls = pd.read_csv(os.path.join(script_dir, 'control_variables_long.csv'))

# Merge the datasets on country_code and year
master_panel = pd.merge(df_gpr, df_controls, on=['country_code', 'year'], how='inner')

# Save the dataset merged
master_panel.to_csv(os.path.join(script_dir, 'master_panel.csv'), index=False)

print(f"Dataset master_panel generado. Países únicos incluidos: {len(master_panel['country_code'].unique())}")

