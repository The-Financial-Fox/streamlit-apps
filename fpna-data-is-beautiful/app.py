import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

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
    st.write("""
    #### When to Use:
    Revenue trends are essential for identifying how revenue evolves over time. FP&A teams can use this analysis
    to monitor seasonality, evaluate growth rates, and detect any unusual patterns that need further investigation.
    """)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Dummy multi-year data for better visuals
    years = ["2020", "2021", "2022"]
    multi_year_data = []
    for year in years:
        year_revenue = df["Revenue"] + np.random.randint(-10, 20, size=len(df))
        for i, month in enumerate(df["Month"]):
            multi_year_data.append({"Month": month, "Year": year, "Revenue": year_revenue[i]})
    multi_year_df = pd.DataFrame(multi_year_data)

    # Plot
    fig, ax = plt.subplots(figsize=(14, 8))
    custom_palette = sns.color_palette("coolwarm", n_colors=len(years))
    sns.lineplot(data=multi_year_df, x="Month", y="Revenue", hue="Year", style="Year", markers=True, linewidth=2.5, palette=custom_palette)

    # Enhance the visualization
    ax.set_title('Revenue Trend Analysis (Multi-Year)', fontsize=20, fontweight='bold')
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Revenue ($)', fontsize=14)
    ax.tick_params(axis='x', labelsize=12, rotation=45)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(title='Year', fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))
    ax.grid(visible=True, linestyle='--', alpha=0.6)
    st.pyplot(fig)


# 2. Expense Analysis
elif analysis_type == "Expense Analysis":
    st.write("""
    #### When to Use:
    Expense analysis helps FP&A teams understand cost drivers and identify areas where expenses are increasing.
    This is critical for cost control initiatives, budget adherence, and profitability analysis.
    """)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Plot
    fig, ax = plt.subplots(figsize=(14, 8))
    colors = sns.color_palette("rocket", as_cmap=False)
    sns.barplot(data=df, x="Month", y="Expenses", palette=colors, ax=ax)

    # Enhance the visualization
    ax.set_title('Monthly Expense Analysis', fontsize=20, fontweight='bold')
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Expenses ($)', fontsize=14)
    ax.tick_params(axis='x', labelsize=12, rotation=45)
    ax.tick_params(axis='y', labelsize=12)
    ax.grid(visible=True, linestyle='--', alpha=0.6)
    st.pyplot(fig)


# 3. Profitability Metrics
elif analysis_type == "Profitability Metrics":
    st.write("""
    #### When to Use:
    Profitability metrics allow FP&A teams to measure how effectively the business generates profit
    relative to revenue and costs. It is useful for benchmarking performance and identifying margin improvements.
    """)

    # Interactive Plot with Plotly
    fig = px.bar(
        df,
        x="Month",
        y="Profit",
        title="Profitability Metrics",
        labels={"Profit": "Profit ($)"},
        color="Profit",
        color_continuous_scale="Blues",
    )
    fig.update_layout(
        title_font=dict(size=20, family="Arial"),
        xaxis_title="Month",
        yaxis_title="Profit ($)",
        font=dict(size=14),
        xaxis_tickangle=45,
        template="plotly_white",
    )
    st.plotly_chart(fig)


# 4. Forecast Accuracy
elif analysis_type == "Forecast Accuracy":
    st.write("""
    #### When to Use:
    Use forecast accuracy to compare actual performance against forecasts. This helps FP&A teams
    refine forecasting models and assess whether assumptions were valid for decision-making.
    """)

    # Dummy forecast data
    forecast = [95, 110, 120, 135, 145, 155]

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Plot
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.lineplot(x=df["Month"], y=df["Revenue"], label="Actual Revenue", marker="o", linewidth=2.5, color="blue", ax=ax)
    sns.lineplot(x=df["Month"], y=forecast, label="Forecast Revenue", linestyle="--", marker="o", linewidth=2.5, color="orange", ax=ax)

    # Enhance the visualization
    ax.set_title('Forecast Accuracy', fontsize=20, fontweight='bold')
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Revenue ($)', fontsize=14)
    ax.tick_params(axis='x', labelsize=12, rotation=45)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(title=None, fontsize=12)
    ax.grid(visible=True, linestyle='--', alpha=0.6)
    st.pyplot(fig)


# 5. Cost Structure Analysis
elif analysis_type == "Cost Structure Analysis":
    st.write("""
    #### When to Use:
    Cost structure analysis breaks down total expenses into components, helping FP&A teams
    understand how costs are allocated. This is crucial for identifying inefficiencies and
    optimizing resource allocation.
    """)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Create dummy cost components
    cost_data = pd.DataFrame({
        "Category": ["Salaries", "Marketing", "R&D", "Operations", "Miscellaneous"],
        "Cost": [40, 25, 15, 10, 10]
    })

    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    wedges, texts, autotexts = ax.pie(
        cost_data["Cost"], labels=cost_data["Category"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"),
        textprops=dict(color="black", fontsize=12)
    )
    ax.set_title("Cost Structure Breakdown", fontsize=20, fontweight="bold")
    st.pyplot(fig)

# 6. Revenue by Region
elif analysis_type == "Revenue by Region":
    st.write("""
    #### When to Use:
    Revenue by region analysis helps FP&A teams identify geographical strengths and weaknesses.
    It is useful for prioritizing regions for investment or identifying underperforming areas
    that may need additional focus.
    """)

    # Dummy region-based data
    region_data = pd.DataFrame({
        "Region": ["North", "South", "East", "West"],
        "Revenue": [500, 700, 300, 400]
    })

    # Interactive Plotly Pie Chart
    fig = px.pie(
        region_data,
        names="Region",
        values="Revenue",
        title="Revenue by Region",
        color="Region",
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    fig.update_traces(textinfo="percent+label", pull=[0, 0.1, 0, 0])  # Emphasize "South"
    fig.update_layout(title_font_size=20)
    st.plotly_chart(fig)


# 7. Product Profitability
elif analysis_type == "Product Profitability":
    st.write("""
    #### When to Use:
    Use product profitability analysis to understand which products generate the most profit.
    FP&A teams can leverage this to focus on high-margin products or identify unprofitable
    products to optimize the portfolio.
    """)

    # Dummy product profitability data
    product_data = pd.DataFrame({
        "Product": ["A", "B", "C", "D"],
        "Profit": [200, 300, 100, 150]
    })

    # Seaborn barplot with custom palette
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = sns.color_palette("coolwarm", n_colors=len(product_data))
    sns.barplot(data=product_data, x="Product", y="Profit", palette=colors, ax=ax)

    # Enhance the visualization
    ax.set_title("Product Profitability", fontsize=20, fontweight="bold")
    ax.set_xlabel("Product", fontsize=14)
    ax.set_ylabel("Profit ($)", fontsize=14)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    st.pyplot(fig)


# 8. Customer Segmentation
elif analysis_type == "Customer Segmentation":
    st.write("""
    #### When to Use:
    Customer segmentation allows FP&A teams to group customers by behavior, revenue, or other attributes.
    This helps identify high-value customers or areas where targeted marketing may yield better results.
    """)

    # Dummy segmentation data
    segment_data = pd.DataFrame({
        "Segment": ["Enterprise", "SMB", "Consumer"],
        "Revenue": [800, 500, 300]
    })

    # Interactive Plotly Bar Chart
    fig = px.bar(
        segment_data,
        x="Segment",
        y="Revenue",
        color="Segment",
        title="Customer Segmentation Analysis",
        color_discrete_sequence=px.colors.qualitative.Plotly
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title="Customer Segment",
        yaxis_title="Revenue ($)",
        font=dict(size=14),
        template="plotly_white"
    )
    st.plotly_chart(fig)

# 9. Scenario Analysis
elif analysis_type == "Scenario Analysis":
    st.write("""
    #### When to Use:
    Scenario analysis helps FP&A teams model best-case, worst-case, and base-case scenarios.
    This is especially useful for forecasting and stress-testing financial plans.
    """)

    # Dummy scenario data
    scenario_data = {
        "Scenario": ["Base", "Optimistic", "Pessimistic"],
        "Revenue": [140, 160, 120]
    }
    scenario_df = pd.DataFrame(scenario_data)

    # Interactive Plotly Bar Chart
    fig = px.bar(
        scenario_df,
        x="Scenario",
        y="Revenue",
        title="Scenario Analysis",
        color="Scenario",
        color_discrete_sequence=["#1f77b4", "#2ca02c", "#d62728"]  # Custom colors
    )
    fig.update_layout(
        title_font_size=20,
        xaxis_title="Scenario",
        yaxis_title="Revenue ($)",
        font=dict(size=14),
        template="plotly_white"
    )
    st.plotly_chart(fig)


# 10. Cash Flow Trends
elif analysis_type == "Cash Flow Trends":
    st.write("""
    #### When to Use:
    Cash flow trends are crucial for monitoring liquidity. FP&A teams can use this analysis
    to ensure the business has sufficient cash to meet short-term obligations and plan for investments.
    """)

    # Dummy cash flow data
    cash_flow_data = {
        "Month": df["Month"],
        "Cash Flow": [30, 40, 50, 60, 70, 80]
    }
    cash_flow_df = pd.DataFrame(cash_flow_data)

    # Enhanced Line Chart with Seaborn
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.lineplot(data=cash_flow_df, x="Month", y="Cash Flow", marker="o", linewidth=2.5, color="teal", ax=ax)

    # Enhance the visualization
    ax.set_title("Cash Flow Trends", fontsize=20, fontweight="bold")
    ax.set_xlabel("Month", fontsize=14)
    ax.set_ylabel("Cash Flow ($)", fontsize=14)
    ax.tick_params(axis="x", labelsize=12, rotation=45)
    ax.tick_params(axis="y", labelsize=12)
    ax.grid(visible=True, linestyle="--", alpha=0.6)
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

