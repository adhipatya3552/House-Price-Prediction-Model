import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import pickle

# Get absolute path of current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Move to project root
project_root = os.path.dirname(current_dir)

# Build correct path
model_path = os.path.join(project_root, "models", "model.pkl")

# Load model
model, feature_columns = pickle.load(open(model_path, "rb"))

st.title("Boston House Price Predictor")

st.subheader("Model Info")
st.write("Model: Random Forest Regressor")
st.write("Dataset: Boston Housing Dataset")

input_data = {}

st.subheader("Adjust Property Features")

for col in feature_columns:
    if col in ["RM"]:
        input_data[col] = st.slider(f"{col} (Rooms)", 1.0, 10.0, 5.0)

    elif col in ["LSTAT"]:
        input_data[col] = st.slider(f"{col} (% Lower Income)", 0.0, 40.0, 10.0)

    elif col in ["PTRATIO"]:
        input_data[col] = st.slider(f"{col} (Pupil-Teacher Ratio)", 10.0, 30.0, 18.0)

    elif col in ["CRIM"]:
        input_data[col] = st.slider(f"{col} (Crime Rate)", 0.0, 100.0, 1.0)

    else:
        input_data[col] = st.slider(f"{col}", 0.0, 100.0, 5.0)

if st.button("Predict Price"):
    if input_data["RM"] <= 0:
        st.error("Rooms must be greater than 0")
    else:
        input_df = pd.DataFrame([input_data])
        prediction = model.predict(input_df)

        price = prediction[0] * 1000
        st.success(f"Estimated Price: ${price:,.2f}")

if st.checkbox("Show Feature Importance"):
    importances = model.feature_importances_
    features = feature_columns

    plt.figure(figsize=(8, 6))
    plt.barh(features, importances)
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.title("Feature Importance")

    st.pyplot(plt)        