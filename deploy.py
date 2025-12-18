import streamlit as st
import joblib

st.title("Iris Flower Classifier")

model=joblib.load('knn_model.joblib')
sepal_length= st.number_input(label="Sepal Length", min_value=0.0, max_value=1.0)
sepal_width= st.number_input(label="Sepal width", min_value=0.0, max_value=1.0)
petal_length= st.number_input(label="Petal Length", min_value=0.0, max_value=1.0)
petal_width= st.number_input(label="Petal width", min_value=0.0, max_value=1.0)
sample= [[sepal_length, sepal_width, petal_length, petal_width]]
if st.buttom("Predict"):
    prediction= model.predict(sample)[0]
    st.success(f"Predicted species is {prediction}")
