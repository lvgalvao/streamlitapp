import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
localhost = os.getenv('HOST')
mydatabase = os.getenv('DBNAME')

# Define the connection string
DATABASE_URL = f"postgresql://{username}:{password}@{localhost}:5432/{mydatabase}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the SQL query to fetch data from the sample_table
query = "SELECT * FROM sample_table"

# Use pandas to execute the query and fetch the data
def fetch_data(query):
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)
    return df

# Streamlit application
def main():
    st.title("PostgreSQL Data Viewer")

    st.write("Fetching data from PostgreSQL database...")
    
    # Fetch data
    data = fetch_data(query)
    
    # Display data
    st.dataframe(data)

if __name__ == "__main__":
    main()
