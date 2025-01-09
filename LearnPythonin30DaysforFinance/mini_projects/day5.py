import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def run():
    # Day 5 Header
    st.header("Day 5: Understanding Seasonality and Patterns in Data")

    # Introduction
    st.write("""
    **Welcome to Day 5!**  
    Today, we'll explore seasonality and patterns in data, essential for analyzing and forecasting recurring trends in FP&A.
    
    ### What You’ll Learn:
    - What is seasonality?
    - How to identify patterns in time-series data
    - Practical applications in FP&A
    """)

    # What is Seasonality?
    st.subheader("1. What is Seasonality?")
    st.write("""
    Seasonality refers to recurring patterns or trends in data, often tied to a specific time frame (e.g., monthly, quarterly, yearly).

    Examples:
    - Increased sales during holiday seasons.
    - Recurring expenses in quarterly budgets.
    """)

    st.image(
        "https://miro.medium.com/max/1200/1*7BWehBB-CL4OfFAS0ayLnw.png",
        caption="Visual representation of seasonality and trends in data."
    )

    # Example Dataset: Monthly Revenue
    st.subheader("2. Example Dataset: Monthly Revenue")
    st.write("Below is a sample dataset with monthly revenue, which exhibits seasonality.")
    
    # Create Sample Data
    np.random.seed(42)
    months = pd.date_range(start="2023-01-01", periods=24, freq='M')
    baseline_revenue = 10000
    seasonal_pattern = [1.2, 1.0, 0.8, 1.1] * 6
    noise = np.random.normal(0, 500, len(seasonal_pattern))
    revenue = baseline_revenue * np.array(seasonal_pattern) + noise
    data = pd.DataFrame({"Month": months, "Revenue": revenue})

    # Display Data
    st.dataframe(data)

    # Visualization
    st.subheader("Revenue Over Time")
    fig, ax = plt.subplots()
    ax.plot(data['Month'], data['Revenue'], marker='o', label="Monthly Revenue")
    ax.set_title("Monthly Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Decompose Time-Series Data
    st.subheader("3. Decomposing the Data into Components")
    st.write("""
    To better understand the patterns in data, we can decompose it into:
    - **Trend**: The general direction of the data.
    - **Seasonality**: The recurring patterns.
    - **Residual**: The noise or irregularities.
    """)

    # Decompose using statsmodels
    decomposition = seasonal_decompose(data["Revenue"], period=4, model='multiplicative', extrapolate_trend='freq')

    # Plot Decomposition
    st.write("### Decomposed Components:")
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 12), sharex=True)
    ax1.plot(data["Month"], data["Revenue"], label="Original", color='blue')
    ax1.set_title("Original Data")
    ax2.plot(data["Month"], decomposition.trend, label="Trend", color='green')
    ax2.set_title("Trend")
    ax3.plot(data["Month"], decomposition.seasonal, label="Seasonality", color='orange')
    ax3.set_title("Seasonality")
    ax4.plot(data["Month"], decomposition.resid, label="Residual", color='red')
    ax4.set_title("Residual")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Interactive Forecasting with Seasonality
    st.subheader("4. Interactive Forecasting with Seasonality")
    st.write("""
    Use the seasonal pattern from the data to forecast future revenues.
    """)

    periods_to_forecast = st.number_input(
        "Enter the number of future periods to forecast:", 
        min_value=1, 
        value=6, 
        step=1
    )

    # Generate Forecast
    last_trend = decomposition.trend.dropna().iloc[-1]
    seasonal_cycle = list(decomposition.seasonal[:4])
    forecast = []

    for i in range(periods_to_forecast):
        trend = last_trend
        seasonal = seasonal_cycle[i % len(seasonal_cycle)]
        forecast.append(trend * seasonal)

    forecast_months = pd.date_range(start=data["Month"].iloc[-1] + pd.offsets.MonthEnd(), periods=periods_to_forecast, freq='M')
    forecast_df = pd.DataFrame({"Month": forecast_months, "Forecasted Revenue": forecast})

    # Display Forecast
    st.write("### Forecast Results:")
    st.dataframe(forecast_df)

    # Visualize Forecast
    st.subheader("Forecast Visualization")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], label="Historical Revenue", marker='o')
    ax.plot(forecast_df["Month"], forecast_df["Forecasted Revenue"], label="Forecasted Revenue", marker='o', linestyle='--')
    ax.set_title("Historical and Forecasted Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Great job! Today, you learned how to:
    - Identify seasonality in data.
    - Decompose time-series data into components.
    - Use seasonal patterns for forecasting.
    
    **Next Steps:**  
    Tomorrow, we’ll dive into regression-based forecasting techniques to account for multiple variables.
    """)

    # Call to Action
    st.info("📤 Share your findings on social media using #30DaysOfPythonFP&A!")
