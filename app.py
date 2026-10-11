import streamlit as st
import pickle
import numpy as np
import os

# Set page config for title and icon
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺", layout="centered")

# Function to load CSS from the external file
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.warning(f"CSS file '{file_name}' not found.")

# Load the CSS
load_css('style.css')

# Load the model
try:
    with open('PickleDiabetes_', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'PickleDiabetes_' not found. Please ensure it is in the correct directory.")
    st.stop()

# Header Section
st.title("Diabetes Assessment")
st.write("Enter the patient metrics below for a preliminary diabetes risk prediction.")

# Input Fields using columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Years)", min_value=0, max_value=120, value=30, step=1)
    insu = st.number_input("Insulin Level", min_value=0, value=80, step=1)

with col2:
    mass = st.number_input("BMI (Body Mass Index)", min_value=0.0, value=25.0, step=0.1)
    plas = st.number_input("Plasma Glucose", min_value=0, value=100, step=1)

# Prediction Button and Logic
if st.button("Predict Result"):
    input_data = np.array([[age, mass, insu, plas]])
    
    # Make prediction
    prediction = model.predict(input_data)
    result = prediction[0]

    # Clean divider before results
    st.markdown("---")

    # Logic: Handle both Numbers AND Text safely
    try:
        # 1. Try to convert to a number (for 0 vs 1 logic)
        score = float(result)
        
        if score > 0.5:
            st.error("🩺 **Result: Positive** — High likelihood of Diabetes. Please consult a healthcare professional.")
        else:
            st.success("✅ **Result: Negative** — Low likelihood of Diabetes.")
            
    except ValueError:
        # 2. If it's a WORD (like 'tested_positive'), handle it here
        result_str = str(result).lower()
        if "pos" in result_str or "1" in result_str:
             st.error("🩺 **Result: Positive** — High likelihood of Diabetes. Please consult a healthcare professional.")
        else:
             st.success("✅ **Result: Negative** — Low likelihood of Diabetes.")
