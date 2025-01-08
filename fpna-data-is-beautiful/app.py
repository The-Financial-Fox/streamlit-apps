import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Title and Introduction
st.title("FP&A Data is Beautiful")
st.write("""
Welcome to **FP&A Data is Beautiful**! Explore 20 different ways to analyze FP&A data using intuitive and interactive visuals.
Use the dropdown menu on the left to select an analysis type.
""")

# Sidebar for analysis selection
analysis_type = st.sidebar.selectbox(
    "Select an Analysis Type",
    [
        "Revenue Trends",
        "Expense Analysis",
        "Profitability Metrics",
        "Forecast Accuracy",
        "Cost Structure Analysis",
        "Revenue by Region",
        "Product Profitability",
        "Customer Segmentation",
        "Scenario Analysis",
        "Cash Flow Trends",
        "Headcount Trends",
        "Budget vs. Actuals",
        "Revenue per Employee",
        "Customer Retention",
        "Churn Analysis",
        "Operating Margins",
        "Break-even Analysis",
        "EBITDA Trends",
        "Variance Analysis",
        "Strategic KPIs",
    ]
)

# Example FP&A data (replace with real datasets for your app)
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [100, 120, 130, 140, 150, 160],
    "Expenses": [50, 55, 60, 65, 70, 75],
    "Profit": [50, 65, 70, 75, 80, 85],
    "Region": ["North", "East", "West", "North", "East", "West"],
    "Employees": [10, 12, 11, 13, 14, 12],
}
df = pd.DataFrame(data)

# Render selected analysis
st.write(f"### {analysis_type}")

# 1. Revenue Trends
if analysis_type == "Revenue Trends":
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Revenue"], marker="o", label="Revenue")
    ax.set_title("Revenue Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

# 2. Expense Analysis
elif analysis_type == "Expense Analysis":
    fig, ax = plt.subplots()
    ax.bar(df["Month"], df["Expenses"], color="orange", label="Expenses")
    ax.set_title("Expense Analysis")
    ax.set_xlabel("Month")
    ax.set_ylabel("Expenses ($)")
    ax.legend()
    st.pyplot(fig)

# 3. Profitability Metrics
elif analysis_type == "Profitability Metrics":
    fig = px.bar(
        df,
        x="Month",
        y="Profit",
        title="Profitability Metrics",
        labels={"Profit": "Profit ($)"},
    )
    st.plotly_chart(fig)

# 4. Forecast Accuracy
elif analysis_type == "Forecast Accuracy":
    forecast = [95, 110, 120, 135, 145, 155]
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Revenue"], label="Actual Revenue", marker="o")
    ax.plot(df["Month"], forecast, label="Forecast Revenue", linestyle="--", marker="o")
    ax.set_title("Forecast Accuracy")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

# 5. Cost Structure Analysis
elif analysis_type == "Cost Structure Analysis":
    fig, ax = plt.subplots()
    ax.pie(df["Expenses"], labels=df["Month"], autopct='%1.1f%%', startangle=90)
    ax.set_title("Cost Structure Analysis")
    st.pyplot(fig)

# 6. Revenue by Region
elif analysis_type == "Revenue by Region":
    fig = px.pie(df, names="Region", values="Revenue", title="Revenue by Region")
    st.plotly_chart(fig)

# 7. Product Profitability
elif analysis_type == "Product Profitability":
    products = ["Product A", "Product B", "Product C"]
    profit = [200, 150, 100]
    fig = px.bar(
        x=products,
        y=profit,
        labels={"x": "Product", "y": "Profit ($)"},
        title="Product Profitability",
    )
    st.plotly_chart(fig)

# 8. Customer Segmentation
elif analysis_type == "Customer Segmentation":
    segmentation = {
        "Segment": ["Enterprise", "SMB", "Consumer"],
        "Revenue": [300, 150, 200],
    }
    seg_df = pd.DataFrame(segmentation)
    fig = px.bar(
        seg_df,
        x="Segment",
        y="Revenue",
        title="Customer Segmentation",
        labels={"Revenue": "Revenue ($)"},
    )
    st.plotly_chart(fig)

# 9. Scenario Analysis
elif analysis_type == "Scenario Analysis":
    scenarios = {"Base": 140, "Optimistic": 160, "Pessimistic": 120}
    fig = px.bar(
        x=scenarios.keys(),
        y=scenarios.values(),
        labels={"x": "Scenario", "y": "Revenue ($)"},
        title="Scenario Analysis",
    )
    st.plotly_chart(fig)

# 10. Cash Flow Trends
elif analysis_type == "Cash Flow Trends":
    cash_flow = [30, 40, 50, 60, 70, 80]
    fig, ax = plt.subplots()
    ax.plot(df["Month"], cash_flow, marker="o", label="Cash Flow")
    ax.set_title("Cash Flow Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Cash Flow ($)")
    ax.legend()
    st.pyplot(fig)

# 11. Headcount Trends
elif analysis_type == "Headcount Trends":
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Employees"], marker="o", color="purple", label="Employees")
    ax.set_title("Headcount Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Employees")
    ax.legend()
    st.pyplot(fig)

# 12. Budget vs. Actuals
elif analysis_type == "Budget vs. Actuals":
    budget = [90, 110, 120, 130, 140, 150]
    fig, ax = plt.subplots()
    ax.bar(df["Month"], budget, label="Budget", alpha=0.7, color="green")
    ax.bar(df["Month"], df["Revenue"], label="Actual Revenue", alpha=0.7, color="blue")
    ax.set_title("Budget vs. Actuals")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    ax.legend()
    st.pyplot(fig)

# 13. Revenue per Employee
elif analysis_type == "Revenue per Employee":
    df["Revenue per Employee"] = df["Revenue"] / df["Employees"]
    fig, ax = plt.subplots()
    ax.bar(df["Month"], df["Revenue per Employee"], color="teal")
    ax.set_title("Revenue per Employee")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue per Employee ($)")
    st.pyplot(fig)

# 14. Customer Retention
elif analysis_type == "Customer Retention":
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    retention_rate = [90, 85, 80, 82, 85, 88]  # Example retention rates
    fig, ax = plt.subplots()
    ax.plot(months, retention_rate, marker="o", label="Retention Rate (%)", color="green")
    ax.set_title("Customer Retention Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("Retention Rate (%)")
    ax.legend()
    st.pyplot(fig)

# 15. Churn Analysis
elif analysis_type == "Churn Analysis":
    churn_rate = [10, 15, 20, 18, 15, 12]  # Example churn rates
    fig, ax = plt.subplots()
    ax.plot(df["Month"], churn_rate, marker="o", label="Churn Rate (%)", color="red")
    ax.set_title("Churn Analysis")
    ax.set_xlabel("Month")
    ax.set_ylabel("Churn Rate (%)")
    ax.legend()
    st.pyplot(fig)

# 16. Operating Margins
elif analysis_type == "Operating Margins":
    df["Operating Margin"] = (df["Profit"] / df["Revenue"]) * 100
    fig, ax = plt.subplots()
    ax.plot(df["Month"], df["Operating Margin"], marker="o", label="Operating Margin (%)", color="gold")
    ax.set_title("Operating Margins")
    ax.set_xlabel("Month")
    ax.set_ylabel("Operating Margin (%)")
    ax.legend()
    st.pyplot(fig)

# 17. Break-even Analysis
elif analysis_type == "Break-even Analysis":
    sales = [100, 120, 130, 140, 150, 160]
    fixed_costs = 50
    variable_costs = [30, 40, 50, 60, 70, 80]
    profit = [s - (vc + fixed_costs) for s, vc in zip(sales, variable_costs)]
    fig, ax = plt.subplots()
    ax.plot(df["Month"], profit, marker="o", label="Profit")
    ax.axhline(0, linestyle="--", color="red", label="Break-even")
    ax.set_title("Break-even Analysis")
    ax.set_xlabel("Month")
    ax.set_ylabel("Profit ($)")
    ax.legend()
    st.pyplot(fig)

# 18. EBITDA Trends
elif analysis_type == "EBITDA Trends":
    ebitda = [60, 70, 75, 80, 85, 90]  # Example EBITDA values
    fig, ax = plt.subplots()
    ax.bar(df["Month"], ebitda, color="blue")
    ax.set_title("EBITDA Trends")
    ax.set_xlabel("Month")
    ax.set_ylabel("EBITDA ($)")
    st.pyplot(fig)

# 19. Variance Analysis
elif analysis_type == "Variance Analysis":
    actual = [100, 120, 130, 140, 150, 160]
    budget = [90, 110, 120, 130, 140, 150]
    variance = [a - b for a, b in zip(actual, budget)]
    fig, ax = plt.subplots()
    ax.bar(df["Month"], variance, color="orange")
    ax.set_title("Variance Analysis")
    ax.set_xlabel("Month")
    ax.set_ylabel("Variance ($)")
    st.pyplot(fig)

# 20. Strategic KPIs
elif analysis_type == "Strategic KPIs":
    kpis = {
        "KPI": ["Revenue Growth", "Gross Margin", "Net Profit Margin"],
        "Value": [15, 60, 12],  # Example KPI values
    }
    kpi_df = pd.DataFrame(kpis)
    fig = px.bar(
        kpi_df,
        x="KPI",
        y="Value",
        title="Strategic KPIs",
        labels={"Value": "Percentage (%)"},
    )
    st.plotly_chart(fig)

