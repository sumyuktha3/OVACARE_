import streamlit as st
import joblib

model = joblib.load('pcos_prediction_model.pkl')

# Function to calculate BMI
def pcos_prediction_app() :
    def calculate_bmi(weight, height):
        if height == 0:
            return 0
        return weight / ((height / 100) ** 2)

    # Function to calculate Waist-Hip Ratio
    def calculate_whr(waist, hip):
        if hip == 0:
            return 0
        return waist / hip

    # Define mapping for categorical values
    categorical_mapping = {'Y': 1, 'N': 0}

    st.markdown("<p style='font-family: Mansalva, serif; color: #FF0100; font-size:30px;'>Enter the details for the following:</p>", unsafe_allow_html=True)
    
    # Input fields for user data
    age = st.number_input('Age (years)')
    weight = st.number_input('Weight (Kg)')
    height = st.number_input('Height (cm)')
    bmi = calculate_bmi(weight, height)
    st.write(f'BMI: {bmi:.2f}')
    pulse_rate = st.number_input('Pulse rate (bpm)')
    rr = st.number_input('Respiration Rate (breaths/min)')
    hb = st.number_input('Hb (g/dl)')
    cycle_length = st.number_input('Cycle Length (days)')
    hip = st.number_input('Hip (inch)')
    waist = st.number_input('Waist (inch)')
    waist_hip_ratio = calculate_whr(waist, hip)
    st.write(f'Waist-Hip Ratio: {waist_hip_ratio:.2f}')
    
    # Convert categorical values to numerical using mapping
    weight_gain = categorical_mapping[st.radio('Weight gain (Y/N)', ['Y', 'N'], index=0)]
    hair_growth = categorical_mapping[st.radio('Hair growth (Y/N)', ['Y', 'N'], index=0)]
    skin_darkening = categorical_mapping[st.radio('Skin darkening (Y/N)', ['Y', 'N'], index=0)]
    hair_loss = categorical_mapping[st.radio('Hair loss (Y/N)', ['Y', 'N'], index=0)]
    pimples = categorical_mapping[st.radio('Pimples (Y/N)', ['Y', 'N'], index=0)]
    fast_food = categorical_mapping[st.radio('Fast food (Y/N)', ['Y', 'N'], index=0)]
    reg_exercise = categorical_mapping[st.radio('Regular Exercise (Y/N)', ['Y', 'N'], index=0)]

    # Predict button
    if st.button('Predict'):
        # Make prediction
        prediction = model.predict([[age, weight, height, bmi, pulse_rate, rr, hb, cycle_length, hip, waist,
                                    waist_hip_ratio, weight_gain, hair_growth, skin_darkening, hair_loss,
                                    pimples, fast_food, reg_exercise]])
        result = 'PCOS' if prediction[0] == 1 else 'No PCOS'
        return result