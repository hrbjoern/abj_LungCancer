import streamlit as st
import numpy as np
import joblib #it most go to the requirements.txt
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.ensemble import RandomForestClassifier


my_pipeline = joblib.load('data/Bjoern_model.pkl')

st.markdown("<h1 style='text-align: center;'>Are you at stroke risk?</h1>", unsafe_allow_html=True)

#important to remember and act fast
st.image('image/stroke-symptoms.jpg')

st.write("Taking a questionnaire to assess your stroke risk is a proactive step towards understanding and managing your health.")

#Gender
gender = st.radio("Gender",
    ["Female", "Male"], index = None)

#Age
age = st.number_input("Age:", step=5)

#BMI
st.write("Calculating the BMI:")
height = st.number_input("Height in meters:", min_value=0.0, step=0.01)
weight = st.number_input("Weight in kilograms:", min_value=0.0, step=0.1)

# Calculate BMI
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.markdown(f"<h4>Your BMI is: {bmi:.2f}</h4>", unsafe_allow_html=True)

#Heart disease history
heart_disease_yn = st.radio("Ever had a heart disease:",
    ["No", "Yes"], index = None)
#Convert the choice to 0 or 1
heart_disease = 1 if heart_disease_yn == 'Yes' else 0

#Hypertension
hypertension_yn = st.radio("Do you have hypertension:",
    ["No", "Yes"], index = None)
# Convert the choice to 0 or 1
hypertension = 1 if hypertension_yn == 'Yes' else 0

#Married
ever_married = st.radio("Ever married:",
    ["Yes", "No"], index = None)

#Smoking status
smoking_status_c = st.radio("Smoking history:",
    ["never smoked", "formerly smoked", "smokes", "I don't want to answer"], index = None)
#convert "I don't want to answer" to unknown
# Convert "I don't want to answer" to "unknown"
if smoking_status_c == "I don't want to answer":
    smoking_status = 'unknown'
else:
    smoking_status = smoking_status_c
    

#Residence type
Residence_type = st.radio("Residence type:",
    ["Urban", "Rural"], index = None)

#Work type
work_type = st.radio("Work type:",
    ["Private", "Self-employed", "children", "Govt_job", "Never_worked" ], index = None)

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
   # Just for test: st.write(f"Prediction: {prediction[0]}")
    if prediction[0] == 1:
        st.markdown("""<h3 style='color: red;'>You are at stroke risk, please consult with your health professional.</h3>""", unsafe_allow_html=True)
        st.image('image/stroke.jpg')
    else:
        st.markdown("""<h3 style='color: black;'>You are NOT at stroke risk..</h3>""", unsafe_allow_html=True)
        
    st.markdown("<small>The information provided in this content is for informational purposes only and is not intended as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read here. If you think you may have a medical emergency, call your doctor or 112 immediately.</small>", unsafe_allow_html=True)
