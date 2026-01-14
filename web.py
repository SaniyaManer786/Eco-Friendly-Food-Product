import streamlit as st
import numpy as np
import pickle

# Load model
loaded_model = pickle.load(open(r"C:/Users/saniya maner/OneDrive/Desktop/Food_project/model.pkl", 'rb'))

def eco_food_prediction(input_data):
    # Convert to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape for single prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    # Prediction
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return "✅ The food product is **Eco-Friendly** 🌱"
    else:
        return "❌ The food product is **Not Eco-Friendly**"

def main():
    st.title('🌱 Eco-Food Prediction App')
    
    # Create input fields for all 13 features
    st.header("Enter Product Details")
    
    Claims = st.selectbox("Claims (0-3)", [0, 1, 2, 3], 
                         help="Number of eco-related claims (0=none, 3=many)")
    
    Packaging_Type = st.selectbox("Packaging Type (0=plastic, 1=cardboard, 2=glass)", 
                                 [0, 1, 2])
    
    Packaging_Recyclable = st.selectbox("Packaging Recyclable", [0, 1])
    
    Contains_Chemicals = st.selectbox("Contains Chemicals", [0, 1])
    
    Organic_Claim = st.selectbox("Organic Claim", [0, 1])
    
    Vegan_Claim = st.selectbox("Vegan Claim", [0, 1])
    
    Cruelty_Free = st.selectbox("Cruelty Free", [0, 1])
    
    Biodegradable = st.selectbox("Biodegradable", [0, 1])
    
    Carbon_Footprint_Level = st.selectbox("Carbon Footprint (0=high, 1=low)", [0, 1])
    
    Country_of_Origin = st.selectbox("Country of Origin (0=imported, 1=local)", [0, 1])
    
    Price_INR = st.number_input("Price (INR)", min_value=0.0, value=150.0)
    
    Shelf_Life_Months = st.number_input("Shelf Life (months)", min_value=0.0, value=12.0)
    
    Consumer_Rating = st.slider("Consumer Rating (1-5)", 1.0, 5.0, 4.5)
    
    # Prediction button
    if st.button("🚀 Predict Eco-Friendliness"):
        input_data = (Claims, Packaging_Type, Packaging_Recyclable, Contains_Chemicals,
                     Organic_Claim, Vegan_Claim, Cruelty_Free, Biodegradable,
                     Carbon_Footprint_Level, Country_of_Origin, Price_INR, 
                     Shelf_Life_Months, Consumer_Rating)
        
        result = eco_food_prediction(input_data)
        st.markdown(result)
    
    # Feature explanation
    with st.expander("📋 Feature Information"):
        st.write("""
        **13 Features used:**
        - Claims (0-3)
        - Packaging_Type (0=plastic, 1=cardboard, 2=glass)
        - Packaging_Recyclable (0=no, 1=yes)
        - Contains_Chemicals (0=no, 1=yes)
        - Organic_Claim (0=no, 1=yes)
        - Vegan_Claim (0=no, 1=yes)
        - Cruelty_Free (0=no, 1=yes)
        - Biodegradable (0=no, 1=yes)
        - Carbon_Footprint_Level (0=high, 1=low)
        - Country_of_Origin (0=imported, 1=local)
        - Price_INR
        - Shelf_Life_Months
        - Consumer_Rating (1-5)
        """)

if __name__ == "__main__":
    main()
