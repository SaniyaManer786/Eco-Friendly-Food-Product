# Eco-Friendly Food Product Recommendation System

This project is a Machine Learning based recommendation system that suggests eco-friendly food products.  
The system analyzes food product data and recommends similar sustainable products using machine learning techniques.

## Features

- Recommends eco-friendly food products
- Uses machine learning for product similarity
- Fast recommendations using precomputed similarity matrices
- Built with Streamlit for interactive interface

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

## Dataset

The project uses a dataset containing food product information.

Dataset file:
food_products_dataset2.csv

The dataset may contain details like:
- Product name
- Ingredients
- Categories
- Nutritional or environmental attributes

## Machine Learning Approach

The system uses a **content-based recommendation approach**.

Main steps:
1. Data preprocessing
2. Feature extraction
3. Text vectorization
4. Similarity calculation
5. Product recommendation based on similarity scores

Pre-trained files used in the project:
- model.joblib
- vectorizer.joblib
- similarity_matrix.joblib
- products_df.joblib
- feature_cols.joblib

These files allow the system to generate recommendations without retraining the model.

## Installation

Clone the repository

```
git clone https://github.com/SaniyaManer786/Eco-Friendly-Food-Product.git
```

Go to the project directory

```
cd Eco-Friendly-Food-Product
```

Install required dependencies

```
pip install -r requirements.txt
```

## Run the Project

Run the Streamlit application

```
streamlit run index.py
```

Then open the local link shown in the terminal.

Example:
```
http://localhost:8501
```

## Future Improvements

- Improve recommendation accuracy
- Add more environmental metrics
- Add better filtering options
- Deploy the system online

## Author

Saniya Maner

GitHub:  
https://github.com/SaniyaManer786

## License

This project is for educational purposes.
