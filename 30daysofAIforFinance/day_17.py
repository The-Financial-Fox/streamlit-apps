import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

TITLE = "Advanced Financial Modeling with Sensitivity Analysis"

def day_17_page():
    # Header
    st.title(f"📊 Day 17: {TITLE}")
    st.write("Welcome to Day 17! Today, we will explore advanced financial modeling techniques using sensitivity analysis to understand the impact of input variables on financial outcomes.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Sensitivity Analysis?**")
    st.markdown("- **Building Flexible Financial Models.**")
    st.markdown("- **Applications in FP&A: Forecast Accuracy, Risk Mitigation.**")

    # Sensitivity Analysis Example
    st.header("Sensitivity Analysis Example")
    st.write("Let's analyze how revenue changes with variations in price and volume.")

    # User Inputs
    base_price = st.number_input("Enter base price per unit ($):", min_value=1.0, value=50.0, step=1.0)
    base_volume = st.number_input("Enter base volume of units sold:", min_value=1, value=1000, step=10)

    # Generate Sensitivity Data
    price_range = np.linspace(base_price * 0.8, base_price * 1.2, 10)
    volume_range = np.linspace(base_volume * 0.8, base_volume * 1.2, 10)

    sensitivity_df = pd.DataFrame(
        {
            "Price": np.repeat(price_range, len(volume_range)),
            "Volume": np.tile(volume_range, len(price_range))
        }
    )
    sensitivity_df["Revenue"] = sensitivity_df["Price"] * sensitivity_df["Volume"]

    st.write("Sensitivity Data:")
    st.dataframe(sensitivity_df.head())

    # Visualization
    st.header("Sensitivity Analysis Visualization")
    fig = px.scatter_3d(
        sensitivity_df,
        x="Price",
        y="Volume",
        z="Revenue",
        color="Revenue",
        labels={"Price": "Price ($)", "Volume": "Volume", "Revenue": "Revenue ($)"},
        title="Revenue Sensitivity to Price and Volume"
    )
    st.plotly_chart(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can sensitivity analysis help in understanding financial risks?",
        placeholder="Write your thoughts here...",
        key="day17_q1"
    )

    response_2 = st.text_area(
        "2. What other variables could be included in a sensitivity analysis model?",
        placeholder="Write your examples here...",
        key="day17_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of sensitivity analysis:")
    st.markdown("- [Introduction to Sensitivity Analysis](https://corporatefinanceinstitute.com/resources/knowledge/modeling/what-is-sensitivity-analysis/)")
    st.markdown("- [Plotly 3D Visualization Documentation](https://plotly.com/python/3d-scatter-plots/)")
    st.markdown("- [Advanced Financial Modeling Techniques](https://www.wallstreetmojo.com/financial-modeling-techniques/)")

    st.info("Congratulations on completing Day 17! Tomorrow, we'll dive into advanced forecasting methods using machine learning.")

if __name__ == "__main__":
    day_17_page()
