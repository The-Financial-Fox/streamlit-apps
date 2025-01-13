import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Data Visualization for FP&A"

def day_6_page():
    # Header
    st.title(f"📊 Day 6: {TITLE}")
    st.write("Welcome to Day 6! Today, we'll explore data visualization techniques and their role in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **Why Visualization Matters in FP&A?**")
    st.markdown("- **Common Visualization Techniques:** Bar Charts, Line Charts, and Heatmaps.")
    st.markdown("- **Interactive Dashboards for Finance.**")

    # Generate Sample Data
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=12, freq='M')
    revenue = np.random.randint(5000, 15000, size=12)
    expenses = np.random.randint(2000, 10000, size=12)
    profit = revenue - expenses
    data = pd.DataFrame({"Month": dates, "Revenue": revenue, "Expenses": expenses, "Profit": profit})

    # Visualization Section
    st.header("Visualizing Financial Metrics")

    # Line Chart: Revenue vs. Expenses
    st.subheader("1. Revenue vs. Expenses Over Time")
    fig, ax = plt.subplots()
    ax.plot(data["Month"], data["Revenue"], label="Revenue", marker="o")
    ax.plot(data["Month"], data["Expenses"], label="Expenses", marker="o")
    ax.set_title("Revenue vs. Expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Bar Chart: Monthly Profit
    st.subheader("2. Monthly Profit")
    fig, ax = plt.subplots()
    sns.barplot(x=data["Month"].dt.strftime('%b'), y=data["Profit"], ax=ax, palette="coolwarm")
    ax.set_title("Monthly Profit")
    ax.set_xlabel("Month")
    ax.set_ylabel("Profit ($)")
    st.pyplot(fig)

    # Heatmap: Correlation Matrix
    st.subheader("3. Correlation Heatmap")
    corr_matrix = data[["Revenue", "Expenses", "Profit"]].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    ax.set_title("Correlation Matrix")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can visualizations like bar charts and heatmaps help in financial decision-making?",
        placeholder="Write your thoughts here...",
        key="day6_q1"
    )

    response_2 = st.text_area(
        "2. What additional visualizations could be useful for FP&A?",
        placeholder="Write your examples here...",
        key="day6_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of data visualization techniques:")
    st.markdown("- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)")
    st.markdown("- [Seaborn Documentation](https://seaborn.pydata.org/)")
    st.markdown("- [Best Practices for Data Visualization](https://www.data-to-viz.com/)")

    st.info("Congratulations on completing Day 6! Tomorrow, we'll explore advanced financial modeling techniques.")

if __name__ == "__main__":
    day_6_page()
