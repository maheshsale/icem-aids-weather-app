import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')

st.set_page_config(
    page_title='Weather App', 
    page_icon='🌧️'
)

st.title('☔Weather App')
st.write('Enter the city name and click on the button to get the weather details')

city = st.text_input('Enter the city name')

API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

if st.button('Fetch Weather'):
    with st.spinner():
        response = requests.get(API_URL)
    if(response.status_code == 200):
        data = response.json()
        st.success('Weather Data Fetched Successfully')

        name = data['name']
        country = data['sys']['country']
        st.subheader(f'Weather for {name}, {country}')

        # Extract the weather details in variables
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['main']
        wind_speed = data['wind']['speed']

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric('Temperature', f'🌡️{temperature}°C')
        col2.metric('Humidity', f'💧{humidity}%')
        col3.metric('Weather', f' 🌧{weather}')
        col4.metric('Wind Speed', f'🍃{wind_speed} m/s')
    else:
        st.error('Invalid City Name')
