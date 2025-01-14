import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Advanced Reporting and Data Storytelling"

def day_20_page():
    # Header
    st.title(f"📋 Day 20: {TITLE}")
    st.write("Welcome to Day 20! Today, we will explore advanced reporting techniques and the art of data storytelling to communicate insights effectively.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Data Storytelling?**")
    st.markdown("- **Best Practices for Effective Reporting.**")
    st.markdown("- **Applications in FP&A: Management Reporting, Strategic Communication.**")

    # Simulated Reporting Data
    st.header("Simulated Reporting Data")
    np.random.seed(42)
    departments = ["Sales", "Marketing", "Operations", "Finance", "R&D"]
    revenue = np.random.randint(100000, 500000, size=len(departments))
    expenses = np.random.randint(50000, 300000, size=len(departments))
    profit = revenue - expenses

    df = pd.DataFrame({
        "Department": departments,
        "Revenue": revenue,
        "Expenses": expenses,
        "Profit": profit
    })

    st.write("Sample Data:")
    st.dataframe(df)

    # Visualizations
    st.header("Visualizing Key Metrics")

    # Bar Plot
    st.subheader("Revenue and Expenses by Department")
    fig, ax = plt.subplots()
    df.plot(kind="bar", x="Department", y=["Revenue", "Expenses"], ax=ax)
    ax.set_title("Revenue and Expenses by Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Amount ($)")
    st.pyplot(fig)

    # Profit Distribution
    st.subheader("Profit Distribution")
    fig, ax = plt.subplots()
    sns.barplot(x="Department", y="Profit", data=df, palette="viridis", ax=ax)
    ax.set_title("Profit by Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Profit ($)")
    st.pyplot(fig)

    # Highlight Key Insights
    st.header("Key Insights")
    highest_profit = df.loc[df["Profit"].idxmax()]
    lowest_profit = df.loc[df["Profit"].idxmin()]

    st.write(f"**Department with Highest Profit:** {highest_profit['Department']} ($ {highest_profit['Profit']:,.2f})")
    st.write(f"**Department with Lowest Profit:** {lowest_profit['Department']} ($ {lowest_profit['Profit']:,.2f})")

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can advanced reporting improve decision-making in your organization?",
        placeholder="Write your thoughts here...",
        key="day20_q1"
    )

    response_2 = st.text_area(
        "2. What additional visualizations or metrics could enhance this report?",
        placeholder="Write your examples here...",
        key="day20_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of advanced reporting and data storytelling:")
    st.markdown("- [Introduction to Data Storytelling](https://www.data-to-viz.com/story/)")
    st.markdown("- [Best Practices for Financial Reporting](https://www.corporatefinanceinstitute.com/resources/templates/excel-dashboard/)")
    st.markdown("- [Visualizing Financial Data Effectively](https://www.tableau.com/learn/articles/financial-visualizations)")

    st.info("Congratulations on completing Day 20! Tomorrow, we'll dive into advanced tools for predictive analytics.")

if __name__ == "__main__":
    day_20_page()
