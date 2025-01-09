import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run():
    # Day 8 Header
    st.header("Day 8: Introduction to Time-Series Forecasting")

    # Introduction
    st.write("""
    **Welcome to Day 8!**  
    Today, we’ll start exploring time-series forecasting techniques to predict sequential financial data, like monthly revenue or quarterly expenses.

    ### What You’ll Learn:
    - What is time-series forecasting?
    - Moving averages for trend detection.
    - Forecasting with simple techniques.
    """)

    # What is Time-Series Forecasting?
    st.subheader("1. What is Time-Series Forecasting?")
    st.write("""
    Time-series forecasting analyzes historical data points over time to predict future values.

    Key concepts:
    - **Trend**: The overall direction of the data.
    - **Seasonality**: Recurring patterns or cycles.
    - **Noise**: Random fluctuations in the data.

    Example applications in FP&A:
    - Forecasting monthly revenue.
    - Predicting quarterly expenses.
    - Anticipating cash flow trends.
    """)

    # Example Dataset
    st.subheader("2. Example Dataset: Monthly Revenue")
    st.write("""
    Let’s start with a dataset of monthly revenue over two years.
    """)

    # Create Sample Data
    np.random.seed(42)
    months = pd.date_range(start="2023-01-01", periods=24, freq="M")
    baseline_revenue = 20000
    trend = np.linspace(0, 5000, 24)  # Gradual upward trend
    seasonal_pattern = [1.1, 1.0, 0.9, 1.2] * 6  # Seasonal cycle
    noise = np.random.normal(0, 2000, 24)
    revenue = baseline_revenue + trend + (baseline_revenue * np.array(seasonal_pattern)) + noise

    data = pd.DataFrame({"Month": months, "Revenue": revenue})
    st.dataframe(data)

    # Visualization
    st.subheader("Monthly Revenue Visualization")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], marker="o", label="Monthly Revenue")
    ax.set_title("Monthly Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Moving Averages
    st.subheader("3. Moving Averages for Trend Detection")
    st.write("""
    A moving average smoothens data by calculating the average of overlapping subsets.

    **Why use moving averages?**
    - Detect trends more clearly.
    - Reduce the impact of noise in data.
    """)

    # Compute Moving Averages
    data["3-Month MA"] = data["Revenue"].rolling(window=3).mean()
    data["6-Month MA"] = data["Revenue"].rolling(window=6).mean()

    # Visualization of Moving Averages
    st.write("### Visualization of Moving Averages")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], label="Actual Revenue", marker="o", alpha=0.5)
    ax.plot(data["Month"], data["3-Month MA"], label="3-Month MA", color="orange")
    ax.plot(data["Month"], data["6-Month MA"], label="6-Month MA", color="green")
    ax.set_title("Revenue with Moving Averages")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Simple Forecasting
    st.subheader("4. Forecasting with Moving Averages")
    st.write("""
    Use the moving average of the last few months to forecast future values.
    """)

    periods_to_forecast = st.number_input(
        "Enter the number of future periods to forecast:", 
        min_value=1, 
        value=3, 
        step=1
    )

    # Forecasting with the 3-Month Moving Average
    last_3_month_ma = data["3-Month MA"].iloc[-1]
    forecast_months = pd.date_range(start=data["Month"].iloc[-1] + pd.offsets.MonthEnd(), periods=periods_to_forecast, freq="M")
    forecast_values = [last_3_month_ma] * periods_to_forecast

    forecast_df = pd.DataFrame({"Month": forecast_months, "Forecasted Revenue": forecast_values})

    # Display Forecast
    st.write("### Forecast Results")
    st.dataframe(forecast_df)

    # Visualization of Forecast
    st.subheader("Forecast Visualization")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], label="Historical Revenue", marker="o", alpha=0.5)
    ax.plot(forecast_df["Month"], forecast_df["Forecasted Revenue"], label="Forecasted Revenue", marker="o", linestyle="--", color="red")
    ax.set_title("Historical and Forecasted Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Practical Applications
    st.subheader("5. Practical Applications in FP&A")
    st.write("""
    Moving averages are ideal for:
    - Short-term forecasting.
    - Identifying trends in financial data.
    - Creating baseline projections for budgeting and planning.
    """)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Congratulations! Today, you learned:
    - The basics of time-series forecasting.
    - How to use moving averages for trend detection and forecasting.
    - Practical applications in FP&A.

    **Next Steps:**  
    Tomorrow, we’ll explore **ARIMA models**, a more advanced method for time-series forecasting.
    """)

    # Call to Action
    st.info("📤 Share your insights and forecasts with the hashtag #30DaysOfPythonFP&A!")
