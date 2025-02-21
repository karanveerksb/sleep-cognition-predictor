import streamlit as st
import joblib
import pandas as pd

# Load model
pipeline = joblib.load('best_model.pkl')

# App UI
st.title('Cognitive Performance Predictor')
st.markdown("Predict Stroop Task Reaction Time Based on Sleep & Lifestyle Metrics")

# Input widgets (3 columns for better layout)
col1, col2, col3 = st.columns(3)
with col1:
    sleep_hours = st.slider('Sleep Hours', 3.0, 9.0, 7.0)
    sleep_quality = st.slider('Sleep Quality (0-20)', 0, 20, 10)
    daytime_sleepiness = st.slider('Daytime Sleepiness (0-24)', 0, 24, 10)
with col2:
    age = st.slider('Age', 18, 100, 30)
    bmi = st.slider('BMI', 15.0, 40.0, 25.0)
    caffeine_intake = st.slider('Caffeine Intake (cups/day)', 0, 5, 1)
with col3:
    physical_activity = st.slider('Physical Activity (0-10)', 0, 10, 5)
    stress_level = st.slider('Stress Level (0-40)', 0, 40, 15)
    gender = st.selectbox('Gender', ['Male', 'Female'])

# Predict button
if st.button('Predict'):
    input_data = pd.DataFrame(
        [[sleep_hours, sleep_quality, daytime_sleepiness, age, gender, bmi, caffeine_intake, physical_activity, stress_level]],
        columns=['Sleep_Hours', 'Sleep_Quality_Score', 'Daytime_Sleepiness', 'Age', 'Gender', 
                 'BMI', 'Caffeine_Intake', 'Physical_Activity_Level', 'Stress_Level']
    )
    prediction = pipeline.predict(input_data)[0]
    st.success(f'**Predicted Reaction Time:** {prediction:.2f} seconds')
    st.info('Lower values indicate better cognitive performance!')

# SHAP explanation
st.subheader('How Do Features Impact Predictions?')
st.image('shap_beeswarm.png')