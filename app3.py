import streamlit as st
import numpy as np  # Fixed: was "numpy as numpy"
import pickle      # Fixed: was "pickel"

# Load model (path looks correct now with raw string r"")
loaded_model = pickle.load(open(r"C:/Users/saniya maner/OneDrive/Desktop/Food_project/model.pkl", 'rb'))

st.title("Eco-Friendly Food Product Predictor 🌱")

# Eco-friendly example input (13 features)
input_data = (0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 150, 12, 4.5)  # Should predict 1 (Eco-Friendly)

# Convert to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape for single prediction
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Prediction
prediction = loaded_model.predict(input_data_reshaped)

# Display result
st.write("**Prediction:**", prediction[0])

if prediction[0] == 1:
    st.success("✅ The food product is **Eco-Friendly** 🌱")
else:
    st.error("❌ The food product is **Not Eco-Friendly**")

# Feature explanation
st.write("**Features used:** Claims, Packaging_Type, Packaging_Recyclable, Contains_Chemicals, Organic_Claim, Vegan_Claim, Cruelty_Free, Biodegradable, Carbon_Footprint_Level, Country_of_Origin, Price_INR, Shelf_Life_Months, Consumer_Rating")
