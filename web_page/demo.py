import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load('pcos_prediction_model.pkl')

# Define the Streamlit app
def main():
    st.title('PCOS Prediction Web App')
    st.write('Enter the details below to predict PCOS.')

    # Input fields for user data
    age = st.number_input('Age (years)')
    weight = st.number_input('Weight (Kg)')
    height = st.number_input('Height (cm)')
    bmi = st.number_input('BMI')
    pulse_rate = st.number_input('Pulse rate (bpm)')
    rr = st.number_input('Respiration Rate (breaths/min)')
    hb = st.number_input('Hb (g/dl)')
    cycle_length = st.number_input('Cycle Length (days)')
    hip = st.number_input('Hip (inch)')
    waist = st.number_input('Waist (inch)')
    waist_hip_ratio = st.number_input('Waist:Hip Ratio')
    weight_gain = st.selectbox('Weight gain (Y/N)', ['Y', 'N'])
    hair_growth = st.selectbox('Hair growth (Y/N)', ['Y', 'N'])
    skin_darkening = st.selectbox('Skin darkening (Y/N)', ['Y', 'N'])
    hair_loss = st.selectbox('Hair loss (Y/N)', ['Y', 'N'])
    pimples = st.selectbox('Pimples (Y/N)', ['Y', 'N'])
    fast_food = st.selectbox('Fast food (Y/N)', ['Y', 'N'])
    reg_exercise = st.selectbox('Regular Exercise (Y/N)', ['Y', 'N'])

    # Predict button
    if st.button('Predict'):
        # Make prediction
        prediction = model.predict([[age, weight, height, bmi, pulse_rate, rr, hb, cycle_length, hip, waist,
                                      waist_hip_ratio, weight_gain, hair_growth, skin_darkening, hair_loss,
                                      pimples, fast_food, reg_exercise]])
        result = 'PCOS' if prediction[0] == 1 else 'No PCOS'
        st.write(f'Prediction: {result}')

if __name__ == '__main__':
    main()
