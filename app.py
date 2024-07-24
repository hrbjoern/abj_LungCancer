import streamlit as st
import numpy as np
import joblib #it most go to the requirements.txt
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.ensemble import RandomForestClassifier


my_pipeline = joblib.load('data/pipeline_model.pkl')

st.header('Are you at stroke risk?')

#important to remember and act fast
st.image('image/stroke-symptoms.jpg')

st.write("Taking a questionnaire to assess your stroke risk is a proactive step towards understanding and managing your health.")

#Gender
gender = st.radio("Gender",
    ["Female", "Male"], index = None)

#Age
age = st.number_input("Age:", step=5)

#BMI
st.write("Things for calculting the BMI")
height = st.number_input("Height [m]:", min_value=0.0, step=0.01)
weight = st.number_input("Weight [kg]:", min_value=0.0, step=0.1)

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.markdown(f"<h4>Your BMI is: {bmi:.2f}</h4>", unsafe_allow_html=True)

#Heart disease history
heart_disease = st.radio("Ever had a heart disease:",
    ["0", "1"], index = None)

#Hypertension
hypertension = st.radio("Do you have hypertension:",
    ["0", "1"], index = None)

#Married
ever_married = st.radio("Ever married:",
    ["Yes", "No"], index = None)

#Smoking status
smoking_status = st.radio("Smoking history:",
    ["never smoked", "formerly smoked", "smokes"], index = None)

#Residence type
Residence_type = st.radio("Residence type:",
    ["Urban", "Rural"], index = None)

#Work type
work_type = st.radio("Work type:",
    ["Private", "Self-employed"], index = None)


# When the user clicks the 'Predict' button
if st.button("Predict"):
    # Create an array of inputs for prediction
    input_data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, bmi, smoking_status]])
    # Define the column names for the DataFrame
    column_names = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'bmi', 'smoking_status']
    # Convert the NumPy array to a pandas DataFrame
    df = pd.DataFrame(data=input_data, columns=column_names)


    # Make a prediction using the model
    prediction = my_pipeline.predict(df)
    
    # Display the prediction
    st.write(f"Prediction: {prediction[0]}")



    #if prediction=yes
        #st.write("Taking a questionnaire to assess your stroke risk is a proactive step towards understanding and managing your health.")
    #elif
        #st.write("You are NOT at stroke risk")