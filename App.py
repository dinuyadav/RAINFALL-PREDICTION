import streamlit as st
import pandas as pd
import pickle
import joblib

# Load CSS file
#with open("style.css" ) as f:
#    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Streamlit app title
st.title("RAINFALL PREDICTION BY AI5")

# Load the trained model and feature names from the pickle file
with open("rainfall_prediction_model.pkl", "rb" ) as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

# Collect user inputs with default values to avoid empty strings
i1 = st.text_input('Enter Pressure value', placeholder='2.0', value='2.0')
i2 = st.text_input('Enter Dewpoint', placeholder='2.0', value='2.0')
i3 = st.text_input('Enter Humidity', placeholder='94.0', value='94.0')
i4 = st.text_input('Enter Cloud', placeholder='100.0', value='100.0')
i5 = st.text_input('Enter Sunshine', placeholder='2.0', value='2.0')
i6 = st.text_input('Enter Wind direction', placeholder='55.0', value='55.0')
i7 = st.text_input('Enter Wind speed', placeholder='115.0', value='115.0')

# Convert inputs to float values, handle empty inputs gracefully
try:
    i1 = float(i1)
    i2 = float(i2)
    i3 = float(i3)
    i4 = float(i4)
    i5 = float(i5)
    i6 = float(i6)
    i7 = float(i7)
except ValueError:
    st.error("Please enter valid numeric values.")
    st.stop()  # Stop execution if there is a ValueError

# When the "Predict" button is pressed
if st.button('Predict'):
    # Create input DataFrame for model prediction
    input_data = [i1, i2, i3, i4, i5, i6, i7]
    input_df = pd.DataFrame([input_data], columns=['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'winddirection', 'windspeed'])

    # Make the prediction
    prediction = model.predict(input_df)

    # Display result based on prediction
    if prediction[0] == 1:  # If the prediction is 1 (Rainfall)
        p = "There is a high chance of rainfall, so enjoy your tea with snacks."
        st.image('./istockphoto-1257951336-612x612.jpg')  # Ensure the image path is correct
    else:  # If the prediction is 0 (No Rainfall)
        p = "There is no rain, enjoy the sunny day."
        st.image('./clouds-1117584_640.jpg')  # Ensure the image path is correct

    # Display the result message
    st.text(p)
