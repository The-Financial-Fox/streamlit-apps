import streamlit as st
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

TITLE = "Time-Series Analysis in FP&A"

def day_4_page():
    # Header
    st.title(f"📈 Day 4: {TITLE}")
    st.write("Welcome to Day 4! Today, we'll explore the basics of time-series analysis and its applications in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Time-Series Data?**")
    st.markdown("- **Common Time-Series Analysis Methods:** Moving Averages, Trend Analysis, and Forecasting with Prophet.")
    st.markdown("- **Applications in FP&A:** Revenue forecasting, expense tracking, and anomaly detection.")

    # Time-Series Forecasting with Prophet
    st.header("Time-Series Forecasting with Prophet")
    st.write("Below is an example of using Prophet for time-series forecasting. We'll simulate some revenue data and make predictions for future trends.")

    # Simulate data
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=100)
    revenue = np.cumsum(np.random.randn(100) * 100 + 500)  # Random walk data
    df = pd.DataFrame({"ds": dates, "y": revenue})

    # Fit Prophet model
    model = Prophet()
    model.fit(df)

    # Make future dataframe
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    # Plot forecast
    fig = model.plot(forecast)
    ax = fig.gca()
    ax.set_title("Revenue Forecast using Prophet")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue ($)")
    plt.xticks(rotation=45)

    # Display plot in Streamlit
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can forecasting models like Prophet help in FP&A?",
        placeholder="Write your thoughts here...",
        key="day4_q1"
    )

    response_2 = st.text_area(
        "2. What specific financial metrics would benefit most from time-series forecasting?",
        placeholder="Write your examples here...",
        key="day4_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of time-series analysis and Prophet:")
    st.markdown("- [Introduction to Time-Series Analysis](https://otexts.com/fpp2/)")
    st.markdown("- [Prophet Documentation](https://facebook.github.io/prophet/)")
    st.markdown("- [Pandas Documentation](https://pandas.pydata.org/)")

    st.info("Congratulations on completing Day 4! Tomorrow, we'll dive into forecasting techniques.")

if __name__ == "__main__":
    day_4_page()
