import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run():
    # Day 7 Header
    st.header("Day 7: Multiple Regression for Forecasting")

    # Introduction
    st.write("""
    **Welcome to Day 7!**  
    Today, we’ll explore **multiple regression**, a technique for analyzing relationships between a dependent variable and multiple independent variables. This is essential for complex FP&A scenarios.
    
    ### What You’ll Learn:
    - What is multiple regression?
    - Building and interpreting a multiple regression model.
    - Practical applications in FP&A.
    """)

    # What is Multiple Regression?
    st.subheader("1. What is Multiple Regression?")
    st.write("""
    Multiple regression models the relationship between one dependent variable and multiple independent variables.

    ### Formula:
    \[
    y = b_0 + b_1x_1 + b_2x_2 + ... + b_nx_n
    \]
    Where:
    - \( y \): Dependent variable (e.g., revenue).
    - \( x_1, x_2, ..., x_n \): Independent variables (e.g., marketing spend, headcount, price).
    - \( b_0 \): Intercept.
    - \( b_1, b_2, ..., b_n \): Coefficients for each variable.
    """)

    # Example Dataset
    st.subheader("2. Example Dataset: Revenue Forecasting")
    st.write("""
    Let’s analyze a dataset with three independent variables:
    - **Marketing Spend ($)**: Budget allocated for marketing.
    - **Headcount**: Number of employees working on the product.
    - **Product Price ($)**: Selling price of the product.

    The dependent variable is **Revenue ($)**.
    """)

    # Create Sample Data
    np.random.seed(42)
    n = 50
    marketing_spend = np.random.uniform(5000, 20000, n)
    headcount = np.random.randint(5, 50, n)
    product_price = np.random.uniform(20, 100, n)

    # Create Revenue with Noise
    revenue = (
        3.5 * marketing_spend +
        2000 * headcount +
        150 * product_price +
        np.random.normal(0, 5000, n)
    )

    data = pd.DataFrame({
        "Marketing Spend": marketing_spend,
        "Headcount": headcount,
        "Product Price": product_price,
        "Revenue": revenue
    })

    # Display Data
    st.dataframe(data)

    # Building the Model
    st.subheader("3. Building a Multiple Regression Model")
    st.write("""
    We’ll use the dataset above to create a multiple regression model to predict revenue.
    """)

    # Split Data
    X = data[["Marketing Spend", "Headcount", "Product Price"]]
    y = data["Revenue"]

    # Fit Model
    model = LinearRegression()
    model.fit(X, y)

    # Model Coefficients
    intercept = model.intercept_
    coefficients = model.coef_
    st.write("### Model Equation:")
    st.write(f"Revenue = {intercept:.2f} + {coefficients[0]:.2f} * Marketing Spend + {coefficients[1]:.2f} * Headcount + {coefficients[2]:.2f} * Product Price")

    # Model Predictions
    data["Predicted Revenue"] = model.predict(X)

    # Visualization
    st.subheader("4. Comparing Actual vs Predicted Revenue")
    fig, ax = plt.subplots()
    ax.scatter(data["Revenue"], data["Predicted Revenue"], color='blue', alpha=0.7)
    ax.plot([data["Revenue"].min(), data["Revenue"].max()], [data["Revenue"].min(), data["Revenue"].max()], color='red', linestyle="--", label="Perfect Prediction")
    ax.set_title("Actual vs Predicted Revenue")
    ax.set_xlabel("Actual Revenue ($)")
    ax.set_ylabel("Predicted Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Interactive Forecasting
    st.subheader("5. Interactive Forecasting")
    st.write("""
    Enter values for **Marketing Spend**, **Headcount**, and **Product Price** to forecast revenue.
    """)

    new_marketing = st.number_input("Marketing Spend ($):", min_value=0, value=10000, step=500)
    new_headcount = st.number_input("Headcount:", min_value=1, value=10, step=1)
    new_price = st.number_input("Product Price ($):", min_value=0.0, value=50.0, step=0.5)

    new_data = np.array([[new_marketing, new_headcount, new_price]])
    predicted_revenue = model.predict(new_data)[0]
    st.write(f"### Predicted Revenue: ${predicted_revenue:,.2f}")

    # Model Performance
    st.subheader("6. Model Performance Metrics")
    st.write("""
    Evaluate the model using:
    - **Mean Squared Error (MSE)**: Average squared difference between actual and predicted values.
    - **R-Squared (R²)**: Proportion of variance explained by the model.
    """)
    mse = mean_squared_error(y, data["Predicted Revenue"])
    r2 = r2_score(y, data["Predicted Revenue"])
    st.write(f"### Mean Squared Error (MSE): {mse:,.2f}")
    st.write(f"### R-Squared (R²): {r2:.2f}")

    # Practical Applications
    st.subheader("7. Practical Applications in FP&A")
    st.write("""
    Multiple regression is ideal for:
    - Forecasting revenue based on multiple factors like marketing spend, headcount, and price.
    - Understanding the impact of different variables on financial outcomes.
    - Running "what-if" scenarios to evaluate business strategies.
    """)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Amazing work! Today, you learned:
    - The basics of multiple regression.
    - How to build and interpret a multiple regression model.
    - Practical applications in FP&A.

    **Next Steps:**  
    Tomorrow, we’ll explore **time-series forecasting** techniques for sequential data like monthly or quarterly trends.
    """)

    # Call to Action
    st.info("📤 Share your findings and models with the hashtag #30DaysOfPythonFP&A!")
