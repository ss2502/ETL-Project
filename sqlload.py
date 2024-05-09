import pandas as pd
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn

def load_and_transform_data(file_path):
    # Load the dataset into a DataFrame
    df = pd.read_csv(file_path)

    # Select relevant columns
    columns_of_interest = ['date', 'location', 'total_cases', 'new_cases', 'total_vaccinations', 'people_vaccinated']
    df_filtered = df[columns_of_interest]

    # Convert date column to datetime type
    df_filtered['date'] = pd.to_datetime(df_filtered['date'])

    # Fill missing values
    df_filtered.fillna(method='ffill', inplace=True)

    return df_filtered

def main():
    database = "covid_data.db"
    data_file = "transformed_covid_data.csv"  # Ensure this is the correct path to your transformed data

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # Load and transform data
        df_filtered = load_and_transform_data(data_file)

        # Load data into SQLite database
        df_filtered.to_sql('covid_stats', conn, if_exists='replace', index=False)
        print("Data loaded into SQLite database")

        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
