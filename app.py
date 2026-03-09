import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl","rb"))

st.title("Traffic Congestion Prediction")

st.write("Enter conditions to predict congestion")

temp = st.number_input("Temperature")
rain = st.number_input("Rain (1h)")
snow = st.number_input("Snow (1h)")
clouds = st.number_input("Cloud Coverage")
hour = st.slider("Hour",0,23)
day = st.slider("Day",1,31)
month = st.slider("Month",1,12)
day_of_week = st.slider("Day of Week",0,6)

input_data = pd.DataFrame({
    "temp":[temp],
    "rain_1h":[rain],
    "snow_1h":[snow],
    "clouds_all":[clouds],
    "hour":[hour],
    "day":[day],
    "month":[month],
    "day_of_week":[day_of_week]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(prediction[0])