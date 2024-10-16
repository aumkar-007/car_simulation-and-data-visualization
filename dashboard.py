import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from data_analysis import *
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

df = pd.read_sql("SELECT * FROM car_sim_data", engine)
df2=pd.read_csv("car_sim.csv")

st.title("Car Simulation Data Dashboard")

# Display speed distribution
st.subheader('Speed Distribution')
plot_speed_distribution(df)

# Speed vs Acceleration
st.subheader('Speed vs Acceleration')
plot_speed_vs_acceleration(df)

# Direction vs Speed (Polar Plot)
st.subheader('Direction vs Speed')
plot_polar_direction(df)

# Car Path (Latitude/Longitude)
st.subheader('Car Path by Latitude/Longitude')
st.map(df)

# Proximity Analysis
st.subheader('Proximity Over Time')
plot_proximity(df)

