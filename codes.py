import os
import pickle
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from io import BytesIO

# Helper function to load models from GitHub
def load_model_from_github(url):
    response = requests.get(url)
    model = pickle.load(BytesIO(response.content))
    return model

# URLs to your models on GitHub
diabetes_model_url = 'https://raw.githubusercontent.com/your-username/repository-name/branch-name/diabetes.pkl'
heart_disease_model_url = 'https://raw.githubusercontent.com/your-username/repository-name/branch-name/heart.pkl'
parkinsons_model_url = 'https://raw.githubusercontent.com/your-username/repository-name/branch-name/parkinsons.pkl'

# Load models
diabetes_model = load_model_from_github(diabetes_model_url)
heart_disease_model = load_model_from_github(heart_disease_model_url)
parkinsons_model = load_model_from_github(parkinsons_model_url)

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson’s Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)
