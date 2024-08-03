import streamlit as st
import plotly.express as px
import backend
import pandas as pd

st.header("Weather Forecast")

place = st.text_input("Place: ")
place = place.capitalize()
forecast_days = st.slider("Forecast Days ", min_value=1, max_value=5, help="Select number of days")
kind = st.selectbox("Select data to view", options=['Temperature', 'Sky'])


st.subheader(f"{kind} for the next {forecast_days} day(s) in {place}")

if place:
    try:
        # Get the temperature/sky
        filtered_data= backend.get_data(place, forecast_days)

        # Get the data and create the chart
        match kind:
            case "Temperature":
                temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
                dates = [dict['dt_txt'] for dict in filtered_data]
                df = pd.DataFrame({"Date": dates, "Temperature (C)": temperatures})
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)

            case "Sky":
                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png", "Snow": "images/snow.png"}
                sky_conditions = [skys['weather'][0]['main'] for skys in filtered_data]
                image_path = [images[condition] for condition in sky_conditions]
                st.image(image_path, width=115)
    except KeyError:
        st.info("Enter a valid city name.")