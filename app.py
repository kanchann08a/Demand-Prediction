import pandas as pd
import pickle
import streamlit as st

@st.cache_resource
def load_artifacts():
    with open("xgboost_demand_model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("label_encoders.pkl", "rb") as f:
        encoders = pickle.load(f)

    return model, encoders

model, label_encoders = load_artifacts()

st.title("Demand Forecasting App")
st.divider()

st.header("Input Features")

price = st.number_input(
    "Price",
    min_value=0.0,
    value=100.0,
    step=50.0
)

discount = st.number_input(
    "Discount %",
    min_value=0.0,
    max_value=100.0,
    value=10.0
)

inventory = st.number_input(
    "Inventory Level",
    min_value=0,
    value=100
)

promotion = st.selectbox(
    "Promotion",
    [0, 1]
)

competitor_pricing = st.number_input(
    "Competitor Pricing",
    min_value=0.0,
    value=50.0
)

category = st.selectbox(
    "Category",
    label_encoders["Category"].classes_.tolist()
)

input_data = pd.DataFrame({
    "Price": [price],
    "Promotion": [promotion],
    "Discount": [discount],
    "Inventory Level": [inventory],
    "Category": [label_encoders["Category"].transform([category])[0]],
    "Competitor Pricing": [competitor_pricing]
})

if st.button("Predict Demand"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Demand: {prediction:.2f}")