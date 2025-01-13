import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

TITLE = "Forecasting Techniques in FP&A"

def day_5_page():
    # Header
    st.title(f"📊 Day 5: {TITLE}")
    st.write("Welcome to Day 5! Today, we'll dive into forecasting techniques and their role in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Forecasting?**")
    st.markdown("- **Basic Forecasting Techniques:** Linear Regression and Moving Averages.")
    st.markdown("- **Applications in FP&A:** Revenue forecasting, expense predictions, and KPI trend analysis.")

    # Linear Regression Example
    st.header("Linear Regression for Forecasting")
    st.write("Below is an example of using Linear Regression to forecast future revenue trends based on historical data.")

    # Simulate data
    np.random.seed(42)
    days = np.arange(1, 101).reshape(-1, 1)  # Days as feature
    revenue = 500 + 10 * days.flatten() + np.random.randn(100) * 100  # Linear trend with noise
    future_days = np.arange(101, 121).reshape(-1, 1)  # Future days

    # Fit Linear Regression
    model = LinearRegression()
    model.fit(days, revenue)
    predictions = model.predict(future_days)

    # Plot actual vs predicted
    fig, ax = plt.subplots()
    ax.scatter(days, revenue, color="blue", label="Historical Revenue", alpha=0.6)
    ax.plot(future_days, predictions, color="red", label="Forecasted Revenue", linewidth=2)
    ax.set_title("Revenue Forecast using Linear Regression")
    ax.set_xlabel("Days")
    ax.set_ylabel("Revenue ($)")
    ax.legend()

    # Display plot in Streamlit
    st.pyplot(fig)

    # Metrics
    mse = mean_squared_error(revenue, model.predict(days))
    st.metric("Mean Squared Error of Model", f"{mse:.2f}")

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can regression models help improve accuracy in financial forecasting?",
        placeholder="Write your thoughts here...",
        key="day5_q1"
    )

    response_2 = st.text_area(
        "2. What limitations do simple forecasting models have, and how can they be addressed?",
        placeholder="Write your examples here...",
        key="day5_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of forecasting techniques:")
    st.markdown("- [Linear Regression in Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)")
    st.markdown("- [Understanding Mean Squared Error](https://en.wikipedia.org/wiki/Mean_squared_error)")
    st.markdown("- [Forecasting Methods Overview](https://otexts.com/fpp2/forecasting-methods.html)")

    st.info("Congratulations on completing Day 5! Tomorrow, we'll explore advanced forecasting methods.")

if __name__ == "__main__":
    day_5_page()
