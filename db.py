from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
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

# Define the Base class for the declarative ORM
Base = declarative_base()

# Define a sample table schema
class SampleTable(Base):
    __tablename__ = 'sample_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    salary = Column(Float)

# Create all tables in the Base metadata
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a sample row to the table (optional)
new_row = SampleTable(name='John Doe', age=30, salary=60000.0)
session.add(new_row)
session.commit()

# Close the session
session.close()

print("Table created and sample data inserted successfully.")
