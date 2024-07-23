import streamlit as st

st.header('Are you at stroke risk?')

#important to remember and act fast
st.image('https://comprehensiveprimarycare.com/wp-content/uploads/2022/03/stroke-symptoms-1024x866.jpg')

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
    st.markdown(f"<h3>Your BMI is: {bmi:.2f}</h3>", unsafe_allow_html=True)

#Heart disease history
heart_disease = st.radio("Ever had a heart disease:",
    ["No", "Yes"], index = None)

#Married
married = st.radio("Ever married:",
    ["Married", "Not married"], index = None)

#Smoking status
smoking = st.radio("Smoking history:",
    ["Never smoked", "Formerly smoked", "Smokes"], index = None)

#average Glucose level
#glucose_level = st.number_input("Average glucose level (100-200):", step=20)

#Residence type
residence_type = st.radio("Residence type:",
    ["Urban", "Rural"], index = None)

#Work type
work_type = st.radio("Work type:",
    ["Private", "Self-employed"], index = None)

#Questionare end, evaluation button
st.button("Evaluate")