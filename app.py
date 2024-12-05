import streamlit as st
import pandas as pd
import joblib
import json

st.set_page_config(
    page_title="Fish Life Prediction Showcase Model"
)

#Data Loading
df = pd.read_csv('Realtime-env2.csv')
model = joblib.load('model.pkl')
feature = json.load(open('feature.json','r'))

# Title
st.header("Fish Life Prediction")
st.image('fish.jpg')

# Overview
st.write('# Overview')
st.write("""Predicting whether fish can survive in a given water environment involves leveraging machine learning techniques to analyze various water quality parameters and make informed predictions based on historical data. The chosen parameters, such as nitrate concentration, pH level, ammonia concentration, water temperature, dissolved oxygen content, turbidity, manganese concentration, atmospheric pressure, temperature in Celsius, humidity percentage, and wind speed, serve as features that influence the prediction.""")

# Introduction
st.write('# Introduction')
st.write('Fish are highly sensitive to their aquatic environment, and understanding the conditions under which they thrive is crucial for maintaining healthy aquatic ecosystems. This project focuses on predicting whether fish can survive in a particular water environment using a machine learning model.')

# Features
st.write('# Features')
col = st.columns([3,3])
with col[0]:
    st.write('''    
    ### Nitrate Concentration (NITRATE):
    Represents the concentration of nitrate in parts per million (PPM). High nitrate levels can indicate pollution, affecting fish health.

    ### pH Level (PH):
    pH measures the acidity or alkalinity of the water. Fish have specific pH preferences, and deviations can impact their physiological processes.

    ### Ammonia Concentration (AMMONIA):
    Indicates the concentration of ammonia in milligrams per liter (mg/l). Ammonia levels are critical as high concentrations are toxic to fish.

    ### Water Temperature (TEMP):
    The temperature of the water in Celsius. Fish have temperature preferences, and extremes can affect their metabolic rates and behavior.
    
    ### Dissolved Oxygen Content (DO):
    Measures the amount of oxygen dissolved in water. Fish rely on dissolved oxygen for respiration, and low levels can lead to stress or suffocation.''')

with col[1]:
    st.write('''

    ### Turbidity:
    Represents the cloudiness or haziness of a fluid. Turbidity affects light penetration and, consequently, the aquatic ecosystem.

    ### Manganese Concentration (MANGANESE):
    Indicates the concentration of manganese in milligrams per liter (mg/l). Manganese levels can impact fish health and reproduction.

    ### Atmospheric Pressure (Pressure):
    Represents the air pressure at the water's surface. Changes in atmospheric pressure can affect fish swim bladder function.

    ### Humidity:
    Represents the percentage of humidity in the air. Atmospheric conditions can indirectly affect water parameters.

    #### Wind Speed (WindspeedKmph):
    Represents the speed of the wind in kilometers per hour. Wind can influence water surface turbulence and gas exchange.''')

# Kaggle Link
st.subheader('Kaggle Dataset')
st.markdown("[Fish Life Prediction DataSet](https://www.kaggle.com/datasets/muzamilaslam/fish-life-prediction)")
#DataFrame
st.header("DataFrame")
st.write(df.head())


def user_input():
    st.write('\n\n')
    st.write('# Water Composition')
    col = st.columns([3,3])
    inputter ={}
    
    for val,i in enumerate(feature):
        minimum = df[i].min() - (df[i].min()*0.2)
        maximum = df[i].max() + (df[i].max()*0.2)
        inputter[i] = col[val%2].slider(i,minimum,maximum)
    inputter = pd.DataFrame([inputter])
    return inputter

input = user_input()

if st.button('predict'):
    prediction = model.predict(input)
    
    if prediction == 1:
        prediction = 'Fish Can life in this water environment'
    else:
        prediction = 'Fish Can\'t life in this water environment'
    
    st.header(prediction)