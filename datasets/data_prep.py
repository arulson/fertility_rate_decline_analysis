import pandas as pd
df = pd.read_csv("C:/Users/Yukti/OneDrive/Desktop/MSBA/GT/Sem 1 courses/CSE 6242/Project/CSE6242_fertility_rate_data.csv")
df_new = pd.melt(df, id_vars=['country'], var_name='year', value_name='fertility_rate')
print(df_new.head(5))
df_new.to_csv("C:/Users/Yukti/OneDrive/Desktop/MSBA/GT/Sem 1 courses/CSE 6242/Project/CSE6242_fertility_rate_updated_schema.csv")
