import streamlit as st
import joblib
import pandas as pd
import os
from xgboost import XGBRegressor

# 1. Dynamically calculate the cross-platform path to the models folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(os.path.dirname(BASE_DIR), 'models', 'house_price_model.pkl')

# 2. Load the model cleanly
model = joblib.load(model_path)

# 3. Create the Streamlit Web UI
st.title("House Price Prediction")

overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 10000, 1500)
garage_cars = st.slider("Garage Cars", 0, 5, 2)

# 4. Handle prediction logic
if st.button("Predict"):
    data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars]
    })
    
    prediction = model.predict(data)[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")
