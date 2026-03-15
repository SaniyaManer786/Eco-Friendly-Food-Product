# 🌱 Eco-Friendly Food Product Recommendation System

A **Machine Learning–Based Recommendation System** that suggests eco-friendly food products based on product similarity.
The system analyzes food product attributes and recommends sustainable alternatives using a **content-based recommendation approach**.

---

## 📌 Project Overview

The goal of this project is to help users discover **eco-friendly and sustainable food products** by leveraging machine learning techniques.
By analyzing product information such as ingredients, categories, and environmental attributes, the system identifies similar products and recommends sustainable alternatives.

The application is built with **Streamlit**, providing an interactive and user-friendly interface.

---

## ✨ Key Features

* 🌿 Recommends eco-friendly food products
* 🤖 Uses **machine learning–based similarity matching**
* ⚡ Fast recommendations using **precomputed similarity matrices**
* 🖥️ Interactive **Streamlit web interface**
* 📦 Pre-trained models for instant predictions

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical operations
* **Scikit-learn** – Machine learning algorithms
* **Streamlit** – Web application interface
* **Joblib** – Model serialization and loading

---

## 📊 Dataset

The project uses a dataset containing food product information.

**Dataset file**

```
food_products_dataset2.csv
```

The dataset may include attributes such as:

* Product Name
* Ingredients
* Categories
* Nutritional information
* Environmental or sustainability indicators

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Recommendation System**.

### Workflow

1. **Data Preprocessing**

   * Cleaning and preparing product data

2. **Feature Extraction**

   * Selecting relevant product attributes

3. **Text Vectorization**

   * Converting textual information into numerical vectors

4. **Similarity Computation**

   * Calculating similarity between products

5. **Recommendation Generation**

   * Suggesting products based on similarity scores

---

## 📁 Pre-Trained Model Files

To improve performance and avoid retraining the model each time, the project uses pre-trained files:

* `model.joblib`
* `vectorizer.joblib`
* `similarity_matrix.joblib`
* `products_df.joblib`
* `feature_cols.joblib`

These files allow the system to **generate recommendations quickly**.

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/SaniyaManer786/Eco-Friendly-Food-Product.git
```

### 2️⃣ Navigate to the Project Directory

```
cd Eco-Friendly-Food-Product
```

### 3️⃣ Install Required Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```
streamlit run index.py
```

After running the command, open the local URL displayed in your terminal.

Example:

```
http://localhost:8501
```

---

## 🔮 Future Improvements

* Improve recommendation accuracy using advanced ML techniques
* Incorporate additional environmental impact metrics
* Add advanced filtering and search options
* Deploy the system as an online web application
* Integrate a larger and more diverse dataset

---

## 👩‍💻 Author

**Saniya Maner**

GitHub:
https://github.com/SaniyaManer786

---

## 📜 License

This project is developed for **educational purposes**.
