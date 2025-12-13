import streamlit as st
import pickle
import numpy as np

# Load the model
# NOTE: Ensure the model file name matches exactly what you upload to GitHub!
with open('PickleDiabetes_', 'rb') as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App (Logistic Regression)")
st.write("Enter the patient details below to predict the diabetes class.")

# Input Fields
# Columns: age, mass, insu, plas
age = st.number_input("Age", min_value=0, max_value=120, value=30)
mass = st.number_input("Body Mass Index (mass)", min_value=0.0, value=25.0)
insu = st.number_input("Insulin Level (insu)", min_value=0, value=80)
plas = st.number_input("Plasma Glucose (plas)", min_value=0, value=100)

if st.button("Predict Result"):
    input_data = np.array([[age, mass, insu, plas]])
    prediction = model.predict(input_data)
    
    if prediction[0] >= 0.5:
        st.error("Result: Positive (High chance of Diabetes)")
    else:
        st.success("Result: Negative (Low chance of Diabetes)")
