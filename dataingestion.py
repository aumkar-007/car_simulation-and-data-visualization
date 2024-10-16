import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

df=pd.read_csv("car_sim.csv")
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

df.to_sql('car_sim_data', engine, if_exists='append', index=False)


print("Data uploaded to PostgreSQL server successfully.")