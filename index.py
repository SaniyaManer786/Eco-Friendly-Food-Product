import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Eco Food App", layout="wide")

st.title("🟢 Eco-Friendly Food System")
st.markdown("Navigate using sidebar 👈")

# ================= SIDEBAR =================
st.sidebar.title("📱 Menu")

menu_option = st.sidebar.radio(
    "Choose an option:",
    ["App 2 - Predict Eco", "Web - Recommend Products"],
    index=0
)

# ================= LOAD MODELS =================
@st.cache_resource
def load_prediction_model():
    return joblib.load("model.joblib")   # keep model inside project folder

@st.cache_resource
def load_recommender_model():
    df = joblib.load("products_df.joblib")
    similarity_matrix = joblib.load("similarity_matrix.joblib")
    return df, similarity_matrix

# ================= PAGE 1 : PREDICTION =================
if menu_option == "App 2 - Predict Eco":
    st.header("🌱 Eco-Food Prediction App")

    model = load_prediction_model()

    def eco_food_prediction(input_data):
        input_data = np.asarray(input_data).reshape(1, -1)
        prediction = model.predict(input_data)
        if prediction[0] == 0:
            return "❌ The food product is **Not Eco-Friendly**"
        else:
            return "✅ The food product is **Eco-Friendly** 🌱"

    st.subheader("Enter Product Details")

    col1, col2 = st.columns(2)
    with col1:
        Claims = st.selectbox("Claims (0-3)", [0, 1, 2, 3])
        Packaging_Type = st.selectbox("Packaging Type", [0, 1, 2])
        Packaging_Recyclable = st.selectbox("Packaging Recyclable", [0, 1])
        Contains_Chemicals = st.selectbox("Contains Chemicals", [0, 1])

    with col2:
        Organic_Claim = st.selectbox("Organic Claim", [0, 1])
        Vegan_Claim = st.selectbox("Vegan Claim", [0, 1])
        Cruelty_Free = st.selectbox("Cruelty Free", [0, 1])
        Biodegradable = st.selectbox("Biodegradable", [0, 1])

    col3, col4 = st.columns(2)
    with col3:
        Carbon_Footprint_Level = st.selectbox("Carbon Footprint", [0, 1])
        Country_of_Origin = st.selectbox("Country of Origin", [0, 1])
        Price_INR = st.number_input("Price (₹)", min_value=0.0, value=150.0)

    with col4:
        Shelf_Life_Months = st.number_input("Shelf Life (months)", min_value=0.0, value=12.0)
        Consumer_Rating = st.slider("Consumer Rating", 1.0, 5.0, 4.5)

    if st.button("🚀 Predict Eco-Friendliness", use_container_width=True):
        input_data = (
            Claims, Packaging_Type, Packaging_Recyclable, Contains_Chemicals,
            Organic_Claim, Vegan_Claim, Cruelty_Free, Biodegradable,
            Carbon_Footprint_Level, Country_of_Origin,
            Price_INR, Shelf_Life_Months, Consumer_Rating
        )
        result = eco_food_prediction(input_data)
        st.markdown(result)

# ================= PAGE 2 : RECOMMENDER =================
elif menu_option == "Web - Recommend Products":
    st.header("🟢 Eco-Friendly Product Recommender")

    df, similarity_matrix = load_recommender_model()

    def get_eco_score(row):
        score = 0
        if row['Packaging_Recyclable'] == 'Yes': score += 1
        if row['Contains_Chemicals'] == 'No': score += 1
        if row['Organic_Claim'] == 'Yes': score += 1
        if row['Vegan_Claim'] == 'Yes': score += 1
        if row['Cruelty_Free'] == 'Yes': score += 1
        if row['Biodegradable'] == 'Yes': score += 1
        if row['Carbon_Footprint_Level'] == 'Low': score += 1
        return score

    def recommend(product_name, df, similarity_matrix, top_n=3):
        idx = df[df['Product_Name'].str.contains(product_name, case=False, na=False)].index
        if len(idx) == 0:
            return []
        idx = idx[0]

        input_eco = get_eco_score(df.iloc[idx])
        sim_scores = list(enumerate(similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+6]

        recs = []
        for i, _ in sim_scores:
            alt_eco = get_eco_score(df.iloc[i])
            if alt_eco >= input_eco:
                recs.append({
                    "name": df.iloc[i]['Product_Name'],
                    "id": df.iloc[i]['Product_ID'],
                    "eco": alt_eco,
                    "packaging": df.iloc[i]['Packaging_Type'],
                    "price": df.iloc[i]['Price_INR']
                })
        return recs[:top_n]

    col1, col2 = st.columns([2, 1])
    with col1:
        product = st.text_input("Enter product name:", "Cold Drink")
        if st.button("Recommend Eco Products", use_container_width=True):
            recs = recommend(product, df, similarity_matrix)
            if recs:
                for rec in recs:
                    st.success(f"**{rec['name']}** (ID: {rec['id']})")
                    st.write(f"🌿 Eco: {rec['eco']}/7 | 📦 {rec['packaging']} | 💰 ₹{rec['price']}")
            else:
                st.error("No eco-friendly alternatives found")

    with col2:
        st.metric("Total Products", len(df))
        st.dataframe(df[['Product_Name', 'Packaging_Type', 'Packaging_Recyclable']].head())




