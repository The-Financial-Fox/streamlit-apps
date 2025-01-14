import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

TITLE = "Interactive Dashboards and KPI Tracking"

def day_15_page():
    # Header
    st.title(f"📊 Day 15: {TITLE}")
    st.write("Welcome to Day 15! Today, we will explore building interactive dashboards and tracking key performance indicators (KPIs) for FP&A.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **Why Dashboards are Crucial for FP&A.**")
    st.markdown("- **Designing Effective KPI Dashboards.**")
    st.markdown("- **Visualization Tools for Interactivity.**")

    # Simulated KPI Dataset
    st.header("Simulated KPI Dataset")
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", periods=30)
    revenue = np.random.randint(5000, 15000, size=30)
    expenses = np.random.randint(3000, 12000, size=30)
    profit = revenue - expenses
    df = pd.DataFrame({"Date": dates, "Revenue": revenue, "Expenses": expenses, "Profit": profit})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # KPI Cards
    st.header("KPI Summary")
    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    total_profit = df["Profit"].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Total Expenses", f"${total_expenses:,.2f}")
    col3.metric("Total Profit", f"${total_profit:,.2f}")

    # Line Chart
    st.header("Revenue and Expenses Over Time")
    fig = px.line(df, x="Date", y=["Revenue", "Expenses"], labels={"value": "Amount ($)", "variable": "Metric"}, title="Revenue and Expenses Over Time")
    st.plotly_chart(fig)

    # Bar Chart
    st.header("Daily Profit")
    fig = px.bar(df, x="Date", y="Profit", title="Daily Profit", labels={"Profit": "Profit ($)", "Date": "Date"})
    st.plotly_chart(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. What KPIs are most critical for your organization's financial analysis?",
        placeholder="Write your thoughts here...",
        key="day15_q1"
    )

    response_2 = st.text_area(
        "2. How can interactivity improve the usability of financial dashboards?",
        placeholder="Write your examples here...",
        key="day15_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of dashboards and KPI tracking:")
    st.markdown("- [Effective KPI Dashboards](https://www.tableau.com/learn/articles/kpi-dashboard)")
    st.markdown("- [Using Plotly for Interactive Visualizations](https://plotly.com/python/)")
    st.markdown("- [Best Practices for Dashboard Design](https://www.klipfolio.com/resources/articles/dashboard-best-practices)")

    st.info("Congratulations on completing Day 15! Tomorrow, we'll explore financial scenario planning with advanced tools.")

if __name__ == "__main__":
    day_15_page()
