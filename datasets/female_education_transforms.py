import pandas as pd
from itertools import product

data_path = r"datasets\Datasets_Raw\female_education.csv"
output_data_path = r"datasets\Datasets_Processed\female_years_schooling_filled.csv"

df = pd.read_csv(data_path)

# Create a full range of years for each country and reindex
min_year, max_year = df['year'].min(), df['year'].max()  # Get the year range
years = list(range(min_year, max_year+1))
countries = list(set(df['country']))
combinations = list(product(countries, years))

df_combinations = pd.DataFrame(combinations, columns=['country', 'year'])

merged_df = df_combinations.merge(df, on=['country', 'year'], how="left")
merged_df = merged_df[['year', 'country', 'yr_sch']].rename(columns={'yr_sch': 'female_years_schooling'})
merged_df = merged_df.sort_values(by=['country', 'year'])
merged_df['female_years_schooling'] = merged_df['female_years_schooling'].ffill()

# Save the result to a new CSV file
merged_df.to_csv(output_data_path, index=False)