from sqlalchemy import create_engine

# Create SQLite engine
engine = create_engine('sqlite:///covid_data.db')

# Load data into database
df_filtered.to_sql('covid_stats', con=engine, if_exists='replace', index=False)
print("Data loaded into SQLite database")
