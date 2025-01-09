import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def run():
    # Day 5 Header
    st.header("Day 5: Understanding Seasonality and Patterns in Data")

    # Introduction Section
    st.write("""
    **Welcome to Day 5!**  
    Today, we’ll explore seasonality and patterns in financial data, which are essential for understanding recurring trends.
    
    ### What You’ll Learn:
    - What is seasonality?
    - How to decompose data into trend, seasonality, and residual components.
    - Practical applications in FP&A.
    """)

    # What is Seasonality?
    st.subheader("1. What is Seasonality?")
    st.write("""
    Seasonality refers to recurring patterns in data over a specific time frame, such as monthly or quarterly trends.
    
    **Examples:**
    - Increased revenue during holiday seasons.
    - Regular expense spikes at the start of each quarter.
    """)

    # Example Dataset
    st.subheader("2. Example Dataset: Monthly Revenue")
    st.write("Let’s analyze a dataset that includes seasonal patterns and noise.")
    
    # Generate Sample Data
    np.random.seed(42)
    months = pd.date_range(start="2023-01-01", periods=24, freq='M')
    baseline_revenue = 10000
    seasonal_pattern = [1.2, 1.0, 0.8, 1.1] * 6  # Quarterly seasonality
    noise = np.random.normal(0, 500, len(seasonal_pattern))
    revenue = baseline_revenue * np.array(seasonal_pattern) + noise
    data = pd.DataFrame({"Month": months, "Revenue": revenue})

    # Display Data
    st.dataframe(data)

    # Visualize the Data
    st.subheader("3. Visualizing the Data")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], marker='o', label="Monthly Revenue")
    ax.set_title("Monthly Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Decompose Time-Series Data
    st.subheader("4. Decomposing the Data")
    st.write("""
    To better understand the data, we can decompose it into the following components:
    - **Trend**: The overall direction of the data.
    - **Seasonality**: The recurring patterns.
    - **Residual**: The noise or irregularities.
    """)

    # Decomposition using statsmodels
    decomposition = seasonal_decompose(data["Revenue"], period=4, model='multiplicative', extrapolate_trend='freq')

    # Plot Decomposition
    st.write("### Decomposed Components")
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

    # Forecasting Using Seasonality
    st.subheader("5. Forecasting Future Values")
    st.write("""
    Using the seasonal pattern and the trend, we can forecast future revenue values.
    """)

    # User Input for Forecast Periods
    periods_to_forecast = st.number_input("Enter the number of future periods to forecast:", min_value=1, value=6, step=1)

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
    st.write("### Forecast Results")
    st.dataframe(forecast_df)

    # Visualize the Forecast
    st.subheader("6. Forecast Visualization")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], label="Historical Revenue", marker='o')
    ax.plot(forecast_df["Month"], forecast_df["Forecasted Revenue"], label="Forecasted Revenue", marker='o', linestyle='--', color='red')
    ax.set_title("Historical and Forecasted Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Great job! Today, you learned:
    - What seasonality is and how to identify it in financial data.
    - How to decompose time-series data into trend, seasonality, and residual components.
    - How to use seasonality to forecast future values.

    **Next Steps:**  
    Tomorrow, we’ll dive deeper into regression-based forecasting with multiple variables.
    """)

    # Call to Action
    st.info("📤 Share your findings and insights with the hashtag #30DaysOfPythonFP&A!")
