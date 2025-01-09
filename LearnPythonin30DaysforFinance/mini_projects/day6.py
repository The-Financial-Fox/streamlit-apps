import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run():
    # Day 6 Header
    st.header("Day 6: Regression-Based Forecasting")

    # Introduction
    st.write("""
    **Welcome to Day 6!**  
    Today, we’ll learn about regression-based forecasting, a powerful technique for predicting financial metrics by analyzing relationships between variables.
    
    ### What You’ll Learn:
    - What is regression-based forecasting?
    - Simple linear regression in Python
    - Practical applications in FP&A
    """)

    # What is Regression-Based Forecasting?
    st.subheader("1. What is Regression-Based Forecasting?")
    st.write("""
    Regression-based forecasting models the relationship between variables to predict outcomes.  
    For example:
    - Predicting revenue based on marketing spend.
    - Forecasting expenses based on headcount.
    - Estimating profit margins as a function of revenue.

    ### Simple Linear Regression Formula:
    \[
    y = mx + b
    \]
    Where:
    - \( y \): Dependent variable (e.g., revenue).
    - \( x \): Independent variable (e.g., marketing spend).
    - \( m \): Slope of the line (rate of change).
    - \( b \): Intercept (value of \( y \) when \( x = 0 \)).
    """)

    # Example Dataset: Marketing Spend vs Revenue
    st.subheader("2. Example Dataset: Marketing Spend vs Revenue")
    st.write("""
    Let’s analyze the relationship between marketing spend and revenue using a simple dataset.
    """)

    # Create Sample Data
    np.random.seed(42)
    marketing_spend = np.linspace(1000, 10000, 15)
    noise = np.random.normal(0, 2000, len(marketing_spend))
    revenue = 2.5 * marketing_spend + 10000 + noise

    data = pd.DataFrame({"Marketing Spend": marketing_spend, "Revenue": revenue})

    # Display Data
    st.dataframe(data)

    # Scatter Plot
    st.subheader("Scatter Plot: Marketing Spend vs Revenue")
    fig, ax = plt.subplots()
    ax.scatter(data["Marketing Spend"], data["Revenue"], color='blue', alpha=0.7, label="Data Points")
    ax.set_title("Marketing Spend vs Revenue")
    ax.set_xlabel("Marketing Spend ($)")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Simple Linear Regression
    st.subheader("3. Building a Simple Linear Regression Model")
    st.write("""
    We’ll fit a linear regression model to this data and use it to forecast revenue for future marketing spend.
    """)

    # Fit Linear Regression Model
    X = data["Marketing Spend"].values.reshape(-1, 1)
    y = data["Revenue"].values

    model = LinearRegression()
    model.fit(X, y)

    # Model Parameters
    slope = model.coef_[0]
    intercept = model.intercept_
    st.write(f"### Model Equation: Revenue = {slope:.2f} * Marketing Spend + {intercept:.2f}")

    # Predicted Values
    data["Predicted Revenue"] = model.predict(X)

    # Visualization of Fit
    st.subheader("Regression Line Fit")
    fig, ax = plt.subplots()
    ax.scatter(data["Marketing Spend"], data["Revenue"], color='blue', alpha=0.7, label="Actual Data")
    ax.plot(data["Marketing Spend"], data["Predicted Revenue"], color='red', label="Regression Line")
    ax.set_title("Regression Line: Marketing Spend vs Revenue")
    ax.set_xlabel("Marketing Spend ($)")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Interactive Forecasting
    st.subheader("4. Forecasting Revenue")
    st.write("""
    Use the regression model to forecast revenue based on new marketing spend values.
    """)
    new_spend = st.number_input("Enter new marketing spend ($):", min_value=0, value=5000, step=100)
    predicted_revenue = model.predict(np.array([[new_spend]]))[0]
    st.write(f"### Predicted Revenue: ${predicted_revenue:,.2f}")

    # Model Performance
    st.subheader("5. Model Performance Metrics")
    st.write("""
    Evaluate the accuracy of the model using the following metrics:
    - **Mean Squared Error (MSE)**: Measures average squared difference between actual and predicted values.
    - **R-Squared (R²)**: Indicates how well the model explains the variability of the dependent variable.
    """)
    mse = mean_squared_error(y, data["Predicted Revenue"])
    r2 = r2_score(y, data["Predicted Revenue"])
    st.write(f"### Mean Squared Error (MSE): {mse:,.2f}")
    st.write(f"### R-Squared (R²): {r2:.2f}")

    # Practical Application
    st.subheader("6. Practical Applications in FP&A")
    st.write("""
    Regression-based forecasting is ideal for:
    - Budgeting based on variable relationships (e.g., marketing spend, headcount).
    - Predicting financial metrics with multiple inputs (covered in advanced regression models).
    - Automating what-if analysis.
    """)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Great work! Today, you learned:
    - The basics of regression-based forecasting.
    - How to build and evaluate a simple linear regression model.
    - Practical applications in FP&A.

    **Next Steps:**  
    Tomorrow, we’ll extend this to multiple regression, where we analyze the impact of multiple variables on financial outcomes.
    """)

    # Call to Action
    st.info("📤 Share your insights and forecasts with the hashtag #30DaysOfPythonFP&A!")
