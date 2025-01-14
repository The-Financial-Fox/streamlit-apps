import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

TITLE = "Time-Series Forecasting with ARIMA"

def day_13_page():
    # Header
    st.title(f"⏳ Day 13: {TITLE}")
    st.write("Welcome to Day 13! Today, we will explore time-series forecasting using ARIMA, a powerful model for analyzing and predicting sequential data.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is ARIMA?**")
    st.markdown("- **Components of Time-Series: Trend, Seasonality, Residuals.**")
    st.markdown("- **Applications in FP&A: Forecasting Revenue, Costs, and Demand.**")

    # Simulate Time-Series Data
    st.header("Simulated Time-Series Data")
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=100)
    revenue = 1000 + np.cumsum(np.random.randn(100) * 50)  # Simulated trend data
    df = pd.DataFrame({"Date": dates, "Revenue": revenue})
    df.set_index("Date", inplace=True)

    st.write("Sample Time-Series Data:")
    st.dataframe(df.head())

    # Plot Time-Series
    st.header("Time-Series Plot")
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Revenue"], label="Revenue")
    ax.set_title("Revenue Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Fit ARIMA Model
    st.header("ARIMA Forecasting")
    st.write("We'll use ARIMA to model and forecast the revenue for the next 30 periods.")

    model = ARIMA(df, order=(1, 1, 1))  # Simple ARIMA(1, 1, 1)
    model_fit = model.fit()

    # Forecast
    forecast = model_fit.forecast(steps=30)
    forecast_index = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=30)
    forecast_df = pd.DataFrame({"Forecast": forecast}, index=forecast_index)

    # Plot Forecast
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Revenue"], label="Actual Revenue")
    ax.plot(forecast_df.index, forecast_df["Forecast"], label="Forecasted Revenue", linestyle="--")
    ax.set_title("ARIMA Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can time-series forecasting benefit FP&A processes?",
        placeholder="Write your thoughts here...",
        key="day13_q1"
    )

    response_2 = st.text_area(
        "2. What challenges might arise when forecasting using ARIMA?",
        placeholder="Write your examples here...",
        key="day13_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of ARIMA:")
    st.markdown("- [Introduction to ARIMA](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)")
    st.markdown("- [Time-Series Analysis Basics](https://otexts.com/fpp2/)")
    st.markdown("- [Seasonal Decomposition of Time-Series](https://en.wikipedia.org/wiki/Decomposition_of_time_series)")

    st.info("Congratulations on completing Day 13! Tomorrow, we'll explore optimization techniques for finance.")

if __name__ == "__main__":
    day_13_page()
