# Deployed the model as a streamlit web app 
# Importing the libraries
import streamlit as st
import pandas as pd
import numpy as np
import pickle
# Loading the model
model = pickle.load(open('model_final.pkl', 'rb'))


# Creating the function which will make the prediction using the data which the user inputs
def predict_weather(precipitaion, temp_max, temp_min, wind):
    prediction = model.predict([[precipitaion, temp_max, temp_min, wind]])
    return prediction

# Creating a title and a sub-title
st.title("Weather Prediction App")
st.write("This app predicts the weather condition based on the input parameters")




# Creating a sidebar header
st.sidebar.header('User Input Parameters')

# Creating a function to get the user input
def get_user_input():
    precipitaion = st.sidebar.slider('Precipitaion', 0.0, 60.0, 22.5)
    Temp_min = st.sidebar.slider('Temp_min', -10.0, 28.0, 15.5)
    temp_max = st.sidebar.slider('Temp_max', 0.0, 50.0, 33.2)
    wind_speed = st.sidebar.slider('Wind Speed', 0.0, 20.0, 5.5)
    user_data = {'Precipitation': precipitaion,
                 'Temp_min': Temp_min,
                 'Wind Speed': wind_speed,
                 'Temp_max': temp_max}
    features = pd.DataFrame(user_data, index=[0])
    return features

# Storing the user input into a variable
user_input = get_user_input()
st.subheader("User Input Parameters")
st.write(user_input)




# Creating and storing the result
result = predict_weather(user_input['Precipitation'][0], user_input['Temp_max'][0], user_input['Temp_min'][0], user_input['Wind Speed'][0])
# Output an image based on the result
if result == 'sun':
    st.image('sunny.png', width = 100)
elif result == 'rain':
    st.image('rainy.png', width = 100)
elif result == 'drizzle':
    st.image('drizzle.png', width = 100)
elif result == 'snow':
    st.image('snow2.png', width = 100)
else:
    st.image('fog.png', width = 100)





    