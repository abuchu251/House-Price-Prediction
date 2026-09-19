import streamlit as st
import joblib
from xgboost import XGBRegressor
model = joblib.load(r'..\models\house_price_model.pkl')

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
