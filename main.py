import streamlit as st
import pickle

# Load model
with open("insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Insurance Cost Prediction")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

sex = st.selectbox("Sex", ["female", "male"])
sex = 0 if sex == "female" else 1

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

smoker = st.selectbox("Smoker", ["no", "yes"])
smoker = 0 if smoker == "no" else 1

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

region_mapping = {
    "northeast": 0,
    "northwest": 1,
    "southeast": 2,
    "southwest": 3
}

region = region_mapping[region]

if st.button("Predict Insurance Cost"):

    input_data = [[
        age,
        sex,
        bmi,
        children,
        smoker,
        region
    ]]

    prediction = model.predict(input_data)

    st.success(f"Predicted Insurance Cost: ${prediction[0]:,.2f}")