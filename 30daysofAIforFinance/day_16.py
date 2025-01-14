import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

TITLE = "Scenario Planning for FP&A"

def day_16_page():
    # Header
    st.title(f"📋 Day 16: {TITLE}")
    st.write("Welcome to Day 16! Today, we will explore scenario planning and its role in FP&A for making informed decisions under uncertainty.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Scenario Planning?**")
    st.markdown("- **Creating Financial Scenarios.**")
    st.markdown("- **Applications in FP&A: Risk Analysis, Strategic Decision-Making.**")

    # Simulated Scenario Data
    st.header("Scenario Simulation")
    st.write("Let's simulate three financial scenarios: Optimistic, Pessimistic, and Base Case.")

    np.random.seed(42)
    months = pd.date_range(start="2023-01-01", periods=12, freq='M')
    base_revenue = np.random.randint(8000, 12000, size=12)
    optimistic_revenue = base_revenue * np.random.uniform(1.1, 1.3, size=12)
    pessimistic_revenue = base_revenue * np.random.uniform(0.7, 0.9, size=12)

    df = pd.DataFrame({
        "Month": months,
        "Base": base_revenue,
        "Optimistic": optimistic_revenue,
        "Pessimistic": pessimistic_revenue
    })

    st.write("Simulated Data:")
    st.dataframe(df.head())

    # Visualization
    st.header("Scenario Visualization")
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Base"], label="Base Case", marker="o")
    ax.plot(df["Month"], df["Optimistic"], label="Optimistic", linestyle="--")
    ax.plot(df["Month"], df["Pessimistic"], label="Pessimistic", linestyle="--")
    ax.set_title("Financial Scenarios Over Time")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can scenario planning improve financial decision-making in your organization?",
        placeholder="Write your thoughts here...",
        key="day16_q1"
    )

    response_2 = st.text_area(
        "2. What other variables could be included in a scenario planning model?",
        placeholder="Write your examples here...",
        key="day16_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of scenario planning:")
    st.markdown("- [Scenario Planning Basics](https://hbr.org/1995/11/the-six-steps-to-effective-scenario-planning)")
    st.markdown("- [How to Use Scenario Planning](https://www.mckinsey.com/business-functions/strategy-and-corporate-finance/our-insights/a-ceos-guide-to-scenario-planning)")
    st.markdown("- [Applications in Financial Planning](https://corporatefinanceinstitute.com/resources/knowledge/strategy/scenario-planning/)")

    st.info("Congratulations on completing Day 16! Tomorrow, we'll dive deeper into advanced financial modeling techniques.")

if __name__ == "__main__":
    day_16_page()
