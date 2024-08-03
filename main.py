import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days ", min_value=0, max_value=5, help="Select number of days")

option = st.selectbox("Select data to view", options=['Temperature', 'Sky'])

st.subheader(f"Temperature for the next {days} day(s) in {place}")

st.plotly_chart()