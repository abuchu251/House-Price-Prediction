import streamlit as st
import joblib
from xgboost import XGBRegressor
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(os.path.dirname(BASE_DIR), 'models', 'house_price_model.pkl')
model = joblib.load(model_path)

import sys
st.write(sys.executable)

st.title('House Price Prediction')
import streamlit as st
import joblib
import pandas as pd

model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

overall_qual = st.slider("Overall Quality", 1, 10, 5)
gr_liv_area = st.number_input("Living Area (sq ft)", 500, 10000, 1500)
garage_cars = st.slider("Garage Cars", 0, 5, 2)

if st.button("Predict"):
    
    data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars]
    })
    
    prediction = model.predict(data)[0]
    
    st.success(f"Predicted Price: ${prediction:,.2f}")
