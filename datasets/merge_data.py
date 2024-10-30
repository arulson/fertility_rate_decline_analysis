import pandas as pd

'''# Read the CSV files
daily_income_df = pd.read_csv('updated_daily_income.csv')
gdp_pcap_df = pd.read_csv('updated_gdp_pcap.csv')

# Merge the DataFrames on 'country' and 'year'
merged_df = pd.merge(daily_income_df, gdp_pcap_df, on=['country', 'year'])

# Select and rename the desired output columns
merged_df = merged_df[['country', 'year', 'GDP', 'DailyIncome']]
merged_df = merged_df.rename(columns={'country': 'Country'})

# Save the merged dataset to a new CSV file
merged_file_path = 'merged_data.csv'
merged_df.to_csv(merged_file_path, index=False)

# Display the first few rows of the merged DataFrame
print(merged_df.head())'''


# Load the existing merged data
merged_df = pd.read_csv('merged_data.csv')

# Load the additional CSV file (using the sample data provided)
#additional_df = pd.read_csv("/Users/saranyak/Desktop/GT/Fall2024/DVA/Project/female_years_schooling_filled.csv")
additional_df = pd.read_csv("/Users/saranyak/Desktop/GT/Fall2024/DVA/Project/CSE6242_sex_ratio_updated_schema.csv")
# Ensure column name compatibility
merged_df.rename(columns={'Country': 'country'}, inplace=True)

# Merge the additional DataFrame with the existing data
updated_merged_df = pd.merge(merged_df, additional_df, on=['country', 'year'], how='left')

# Rename columns to match required output
updated_merged_df.rename(columns={'country': 'Country'}, inplace=True)

# Display the first few rows of the updated merged DataFrame
print(updated_merged_df.head())

updated_merged_file_path = 'merged_data.csv'
updated_merged_df.to_csv(updated_merged_file_path, index=False)

print(f"\nUpdated merged data saved to: {updated_merged_file_path}")