# transform.py
import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv('covid_data.csv')

# Select relevant columns
columns_of_interest = ['date', 'location', 'total_cases', 'new_cases', 'total_vaccinations', 'people_vaccinated']
df_filtered = df[columns_of_interest]

# Convert date column to datetime type
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Fill missing values
df_filtered.fillna(method='ffill', inplace=True)

# Optionally, save the transformed data to a new CSV file
df_filtered.to_csv('transformed_covid_data.csv', index=False)

print("Data transformation complete")
