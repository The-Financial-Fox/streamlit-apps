import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TITLE = "Time-Series Analysis in FP&A"

def day_4_page():
    # Header
    st.title(f"📈 Day 4: {TITLE}")
    st.write("Welcome to Day 4! Today, we'll explore the basics of time-series analysis and its applications in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Time-Series Data?**")
    st.markdown("- **Common Time-Series Analysis Methods:** Moving Averages, Trend Analysis, and Seasonal Decomposition.")
    st.markdown("- **Applications in FP&A:** Revenue forecasting, expense tracking, and anomaly detection.")

    # Time-Series Visualization
    st.header("Time-Series Visualization")
    st.write("Below is a simple example of visualizing time-series data. We'll simulate some revenue data and apply a moving average for trend analysis.")

    # Simulate data
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=100)
    revenue = np.cumsum(np.random.randn(100) * 100 + 500)  # Random walk data
    df = pd.DataFrame({"Date": dates, "Revenue": revenue})

    # Calculate moving average
    df["7-Day MA"] = df["Revenue"].rolling(window=7).mean()

    # Plot data
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Revenue"], label="Revenue", alpha=0.7)
    ax.plot(df["Date"], df["7-Day MA"], label="7-Day Moving Average", linewidth=2, linestyle="--")
    ax.set_title("Revenue with Moving Average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)

    # Display plot in Streamlit
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can moving averages help in understanding financial trends?",
        placeholder="Write your thoughts here...",
        key="day4_q1"
    )

    response_2 = st.text_area(
        "2. What other time-series techniques do you think could be useful in FP&A?",
        placeholder="Write your examples here...",
        key="day4_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of time-series analysis:")
    st.markdown("- [Introduction to Time-Series Analysis](https://otexts.com/fpp2/)")
    st.markdown("- [Pandas Rolling and Expanding](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html)")
    st.markdown("- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)")

    st.info("Congratulations on completing Day 4! Tomorrow, we'll dive into forecasting techniques.")

if __name__ == "__main__":
    day_4_page()
