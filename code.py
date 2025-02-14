import pickle

import pandas as pd

# Load the pre-trained model (diabetes_model.pkl)
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))  # Adjust path if needed

# Collect user input
try:
    Pregnancies = float(input("Enter the number of pregnancies: "))
    Glucose = float(input("Enter the glucose level: "))
    Bloodpressure = float(input("Enter the blood pressure value: "))
    SkinThickness = float(input("Enter the skin thickness value: "))
    Insulin = float(input("Enter the insulin level: "))
    BMI = float(input("Enter the BMI value: "))
    DiabetesPedigreeFunction = float(input("Enter the diabetes pedigree function value: "))
    Age = float(input("Enter the age of the person: "))

    # Prepare the input data for prediction
    user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    # Make the prediction
    diab_prediction = diabetes_model.predict([user_input])

    # Output the result
    if diab_prediction[0] == 1:
        print("The person is diabetic.")
    else:
        print("The person is not diabetic.")
except ValueError:
    print("Please enter valid numeric values.")
