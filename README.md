# 📈 Sales Demand Forecasting App

A Machine Learning project that predicts product demand based on pricing, promotions, discounts, inventory levels, competitor pricing, and product category.

Built using Python, XGBoost, Streamlit, and Scikit-Learn.

## 🚀 Features

- Predict future product demand
- Interactive Streamlit web application
- Machine Learning model trained using XGBoost
- Label encoding for categorical features
- Real-time predictions based on user inputs

## 📊 Dataset Features

The model uses the following features:

- Price
- Promotion
- Discount
- Inventory Level
- Competitor Pricing
- Category

Target Variable:

- Demand

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Streamlit
- Pickle

## 📂 Project Structure

```text
sales-forecasting/
│
├── app.py
├── demand_forecasting.csv
├── xgboost_demand_model.pkl
├── label_encoders.pkl
├── requirements.txt
├── analysis.ipynb
├── ml.ipynb
└── README.md
```

## ⚙️ Model Development

The project workflow includes:

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Label Encoding
5. Train-Test Split
6. Model Training using XGBoost Regressor
7. Model Evaluation using:
   - MAE
   - RMSE
   - R² Score
8. Model Serialization using Pickle

## 🎯 Application Workflow

1. Enter product details.
2. Select category and promotion status.
3. Click **Predict Demand**.
4. View the predicted demand instantly.

## 📈 Future Improvements

- Hyperparameter tuning
- Sales trend visualization dashboard
- Cloud deployment
- Model monitoring
- Forecasting for multiple products

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 👩‍💻 Author

Kanchan Nishad

Engineering Student | Web Development | Data Analytics | Machine Learning
