import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run():
    # Day 4 Header
    st.header("Day 4: Forecasting Basics for FP&A")

    # Introduction Section
    st.write("""
    **Welcome to Day 4!**  
    Today, we’ll begin our journey into forecasting. Forecasting is a critical skill in FP&A for predicting future financial outcomes.
    
    ### What You’ll Learn:
    - The concept of forecasting
    - Simple linear forecasting using Python
    - Practical examples and visualizations
    """)

    # Forecasting Basics
    st.subheader("1. What is Forecasting?")
    st.write("""
    Forecasting involves predicting future values based on historical data. It helps in:
    - Budgeting
    - Planning future investments
    - Assessing potential risks and opportunities
    
    **Simple linear forecasting** assumes future growth follows a consistent trend based on historical data.
    """)

    # Example: Simple Linear Forecasting
    st.subheader("2. Example: Simple Linear Forecasting")
    st.write("""
    In simple linear forecasting, we calculate the expected future values based on the average growth rate of past data.
    """)

    # Interactive Example: Forecast Revenue
    st.subheader("Interactive Exercise: Forecast Revenue")
    historical_revenues = st.text_input(
        "Enter historical revenues (comma-separated):", 
        "10000, 12000, 15000, 18000, 21000"
    )
    periods_to_forecast = st.number_input(
        "Enter the number of future periods to forecast:", 
        min_value=1, 
        value=3, 
        step=1
    )

    try:
        # Process Input
        revenue_data = np.array(list(map(float, historical_revenues.split(','))))
        growth_rates = [(revenue_data[i] - revenue_data[i-1]) / revenue_data[i-1] for i in range(1, len(revenue_data))]
        avg_growth_rate = np.mean(growth_rates)

        # Forecast Future Values
        forecast = [revenue_data[-1]]
        for _ in range(periods_to_forecast):
            forecast.append(forecast[-1] * (1 + avg_growth_rate))

        forecast = np.array(forecast)
        forecast_periods = [f"Period {i+1}" for i in range(len(revenue_data) + periods_to_forecast)]

        # Combine Historical and Forecast Data
        combined_data = np.concatenate([revenue_data, forecast[1:]])
        df = pd.DataFrame({"Periods": forecast_periods, "Revenue": combined_data})

        # Display Results
        st.write("### Forecast Results:")
        st.dataframe(df)

        # Visualization
        st.subheader("Revenue Forecast Visualization")
        fig, ax = plt.subplots()
        ax.plot(range(len(revenue_data)), revenue_data, marker='o', label="Historical")
        ax.plot(range(len(revenue_data), len(revenue_data) + periods_to_forecast), forecast[1:], marker='o', label="Forecast", linestyle='--')
        ax.set_title("Revenue Forecast")
        ax.set_xlabel("Period")
        ax.set_ylabel("Revenue")
        ax.legend()
        st.pyplot(fig)

    except ValueError:
        st.error("Please enter valid numeric values for historical revenues.")

    # Practical Application
    st.subheader("3. Practical Applications")
    st.write("""
    Simple linear forecasting is ideal for:
    - Predicting short-term trends.
    - Creating initial budgets or baseline projections.
    
    **Next Steps:**  
    Tomorrow, we’ll build on this and explore advanced techniques like seasonality and regression-based forecasting.
    """)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Congratulations on completing Day 4! You now understand the basics of forecasting and can apply it to short-term revenue predictions.
    """)

    # Call to Action
    st.info("📤 Share your forecast and insights on social media with the hashtag #30DaysOfPythonFP&A!")
