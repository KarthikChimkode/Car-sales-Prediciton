import os
import joblib  # Ensure to use joblib if that's how the model was saved
import streamlit as st

model_path = 'D:/Machine Learning and Data Science/Projects/Car Sales/random_forest_model.pkl'

if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
else:
    st.error("Model file not found! Please check the file path.")

def main():
    st.title('Car Pricing Prediction Solutions')

    # Input Variables
    Year = st.text_input('Year')
    Present_Prices = st.text_input('Present_Price')
    Kms_Driven = st.text_input('Kms_Driven')
    Owner = st.text_input('Owner')
    Fuel_Type_Diesel = st.text_input('Fuel_Type_Diesel')
    Fuel_Type_Petrol = st.text_input('Fuel_Type_Petrol')
    Seller_Type_Individual = st.text_input('Seller_Type_Individual')
    Transmission_Manual = st.text_input('Transmission_Manual')

    # Prediction code
    if st.button('Predict'):
        try:
            # Convert inputs to appropriate data types
            prediction = model.predict([[Year, Present_Prices, Owner, Kms_Driven, Fuel_Type_Diesel, Fuel_Type_Petrol,
                                         Seller_Type_Individual, Transmission_Manual]])
            output = round(prediction[0], 2)
            st.success(f'You Can Sell Your Car For {output}')
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if __name__ == '__main__':
    main()
