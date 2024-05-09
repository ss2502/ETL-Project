# download.py
import pandas as pd

data_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(data_url)
df.to_csv('covid_data.csv', index=False)
print("Data downloaded and saved to csv successfully")
