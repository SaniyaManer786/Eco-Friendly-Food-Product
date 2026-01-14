
import streamlit as st
import pandas as pd
import joblib
import numpy as np

@st.cache_data
def load_model():
    df = joblib.load('products_df.joblib')
    similarity_matrix = joblib.load('similarity_matrix.joblib')
    return df, similarity_matrix

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
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+5]
    
    recs = []
    for i, score in sim_scores:
        alt_eco = get_eco_score(df.iloc[i])
        if alt_eco >= input_eco or df.iloc[i]['Packaging_Recyclable'] == 'Yes':
            recs.append({
                'name': df.iloc[i]['Product_Name'],
                'id': df.iloc[i]['Product_ID'],
                'eco': alt_eco,
                'packaging': df.iloc[i]['Packaging_Type'],
                'price': df.iloc[i]['Price_INR']
            })
    
    return recs[:top_n]

st.set_page_config(page_title="Eco Recommender", layout="wide")
st.title("🟢 Eco-Friendly Product Recommender")

df, similarity_matrix = load_model()

col1, col2 = st.columns([2,1])
with col1:
    product = st.text_input("Enter product name:", "Cold Drink")
    if st.button("Recommend", use_container_width=True):
        recs = recommend(product, df, similarity_matrix)
        if recs:
            for rec in recs:
                st.success(f"**{rec['name']}** (ID: {rec['id']})")
                st.write(f"🌿 Eco: {rec['eco']}/7 | 📦 {rec['packaging']} | 💰 ₹{rec['price']}")
        else:
            st.error("No eco-friendly alternatives found")

with col2:
    st.metric("Products", len(df))
    st.dataframe(df[['Product_Name', 'Packaging_Type', 'Packaging_Recyclable']].head())










