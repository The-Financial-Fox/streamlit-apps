import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.set_page_config(page_title="FP&A Data is Beautiful", layout="wide")

# -----------------------------------------------------------------------------
# Generate Synthetic Data (for demonstration purposes)
# -----------------------------------------------------------------------------

# Setting a random seed for reproducibility
np.random.seed(42)

# Let's assume we have monthly financial data for 3 years (36 months)
date_range = pd.date_range(start='2023-01-01', periods=36, freq='MS')
data = pd.DataFrame({
    'Date': date_range,
    'Revenue': np.random.randint(80000, 150000, 36),
    'COGS': np.random.randint(30000, 80000, 36),
    'Operating_Expenses': np.random.randint(20000, 60000, 36),
    'Marketing_Expenses': np.random.randint(5000, 20000, 36),
    'Number_of_Units_Sold': np.random.randint(1000, 5000, 36),
    'Region': np.random.choice(['North America', 'EMEA', 'APAC', 'LATAM'], 36),
})

# Calculate some derived metrics
data['Gross_Profit'] = data['Revenue'] - data['COGS']
data['Operating_Income'] = data['Gross_Profit'] - data['Operating_Expenses']
data['Net_Income'] = data['Operating_Income'] - data['Marketing_Expenses']

# Split data for yearly aggregation
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month


# -----------------------------------------------------------------------------
# Title and Description
# -----------------------------------------------------------------------------
st.title("FP&A Data is Beautiful")
st.markdown(
    """
    **Welcome to "FP&A Data is Beautiful"!**  
    This Streamlit application showcases 20 visually engaging and interactive ways 
    to analyze financial planning and analysis (FP&A) data.  
    Explore various charts and insights below.
    """
)

# -----------------------------------------------------------------------------
# 1. Time-Series Revenue Trend
# -----------------------------------------------------------------------------
st.header("1. Time-Series Revenue Trend")
st.markdown(
    """
    A simple line chart illustrating **Revenue** over time helps you quickly spot 
    trends, seasonality, and any sudden spikes or dips.
    """
)
fig1 = px.line(data, x='Date', y='Revenue', title="Monthly Revenue Trend")
st.plotly_chart(fig1, use_container_width=True)

# -----------------------------------------------------------------------------
# 2. Gross Profit vs. Operating Income
# -----------------------------------------------------------------------------
st.header("2. Gross Profit vs. Operating Income")
st.markdown(
    """
    A dual-axis chart or side-by-side bar chart highlighting **Gross Profit** and 
    **Operating Income** over time provides a deeper look at cost control and 
    operational efficiency.
    """
)
fig2 = px.bar(data, x='Date', y=['Gross_Profit', 'Operating_Income'],
              barmode='group', title="Gross Profit vs. Operating Income")
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------------------------------------------------
# 3. Waterfall Chart (Revenue to Net Income)
# -----------------------------------------------------------------------------
st.header("3. Waterfall Chart (Revenue to Net Income)")
st.markdown(
    """
    A **waterfall chart** illustrates how you move from **Revenue** down to 
    **Net Income** by subtracting **COGS**, **Operating Expenses**, and 
    **Marketing Expenses**.
    """
)
# For demonstration, we'll just show a single month’s breakdown
latest_month_data = data.iloc[-1]
waterfall_df = pd.DataFrame({
    'Category': ['Revenue', '- COGS', '- Operating Expenses', '- Marketing Expenses', 'Net Income'],
    'Value': [
        latest_month_data['Revenue'],
        -latest_month_data['COGS'],
        -latest_month_data['Operating_Expenses'],
        -latest_month_data['Marketing_Expenses'],
        latest_month_data['Net_Income']
    ]
})
waterfall_df['Running Total'] = waterfall_df['Value'].cumsum()

waterfall_chart = px.bar(
    waterfall_df, x='Category', y='Value',
    title=f"Waterfall Chart for {latest_month_data['Date'].strftime('%b %Y')}",
    text='Value'
)
st.plotly_chart(waterfall_chart, use_container_width=True)

# -----------------------------------------------------------------------------
# 4. Year-over-Year Revenue Comparison
# -----------------------------------------------------------------------------
st.header("4. Year-over-Year Revenue Comparison")
st.markdown(
    """
    An **overlay of yearly revenue** trends allows you to quickly identify 
    seasonal patterns and measure performance vs. prior years.
    """
)
yearly_data = data.groupby(['Year','Month'])['Revenue'].sum().reset_index()
fig4 = px.line(yearly_data, x='Month', y='Revenue', color='Year',
               title="Year-over-Year Monthly Revenue")
st.plotly_chart(fig4, use_container_width=True)

# -----------------------------------------------------------------------------
# 5. Forecast vs. Actuals (Simple Example)
# -----------------------------------------------------------------------------
st.header("5. Forecast vs. Actuals")
st.markdown(
    """
    Compare forecasted revenue against actual revenue. 
    For demonstration, we’ll create a simple linear forecast.
    """
)
df_forecast = data.copy()
df_forecast['Forecast'] = df_forecast['Revenue'].rolling(3).mean().fillna(method='bfill')

fig5 = px.line(df_forecast, x='Date', y=['Revenue', 'Forecast'],
               title="Forecast vs. Actuals (Revenue)")
st.plotly_chart(fig5, use_container_width=True)

# -----------------------------------------------------------------------------
# 6. Gross Margin Heatmap (by Year, Month)
# -----------------------------------------------------------------------------
st.header("6. Gross Margin Heatmap")
st.markdown(
    """
    A **heatmap** displays **Gross Margin** across months and years, helping 
    you see which periods outperformed or underperformed in margin.
    """
)
pivot_data = data.pivot_table(index='Year', columns='Month', values='Gross_Profit', aggfunc='mean')
plt.figure(figsize=(10, 4))
sns.heatmap(pivot_data, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title("Gross Profit Heatmap by Year/Month")
st.pyplot(plt.gcf())
plt.clf()

# -----------------------------------------------------------------------------
# 7. Region-wise Revenue Pie Chart
# -----------------------------------------------------------------------------
st.header("7. Region-wise Revenue Distribution")
st.markdown(
    """
    A **pie chart** or **donut chart** can highlight the share of revenue 
    contributed by each region.
    """
)
region_data = data.groupby('Region')['Revenue'].sum().reset_index()
fig7 = px.pie(region_data, names='Region', values='Revenue',
              title="Revenue by Region", hole=0.4)
st.plotly_chart(fig7, use_container_width=True)

# -----------------------------------------------------------------------------
# 8. Region vs. Revenue Bar Chart
# -----------------------------------------------------------------------------
st.header("8. Region vs. Revenue Bar Chart")
st.markdown(
    """
    A **sorted bar chart** of total revenue by region can instantly show 
    which regions are major contributors.
    """
)
fig8 = px.bar(region_data.sort_values('Revenue', ascending=False),
              x='Region', y='Revenue', title="Total Revenue by Region")
st.plotly_chart(fig8, use_container_width=True)

# -----------------------------------------------------------------------------
# 9. Cost of Goods Sold (COGS) vs. Gross Profit Scatter
# -----------------------------------------------------------------------------
st.header("9. COGS vs. Gross Profit Scatter")
st.markdown(
    """
    A **scatter plot** with **COGS** on one axis and **Gross Profit** on the other 
    can help identify outliers and their impact on profitability.
    """
)
fig9 = px.scatter(data, x='COGS', y='Gross_Profit',
                  color='Region',
                  title="COGS vs. Gross Profit Scatter",
                  labels={'COGS':'Cost of Goods Sold', 'Gross_Profit':'Gross Profit'})
st.plotly_chart(fig9, use_container_width=True)

# -----------------------------------------------------------------------------
# 10. Operating Expenses Breakdown (Stacked Bar)
# -----------------------------------------------------------------------------
st.header("10. Operating Expenses Breakdown (Stacked Bar)")
st.markdown(
    """
    A **stacked bar chart** for **Operating Expenses** vs. **Marketing Expenses** 
    across time can highlight shifts in spending priorities.
    """
)
fig10 = px.bar(data, x='Date', y=['Operating_Expenses','Marketing_Expenses'],
               barmode='stack', title="Operating Expenses Breakdown Over Time")
st.plotly_chart(fig10, use_container_width=True)

# -----------------------------------------------------------------------------
# 11. Rolling 3-Month Average (Revenue, Gross Profit)
# -----------------------------------------------------------------------------
st.header("11. Rolling Averages")
st.markdown(
    """
    A **rolling average** smooths out short-term fluctuations and highlights long-term trends.
    """
)
rolling_window = 3
df_rolling = data[['Date', 'Revenue', 'Gross_Profit']].copy()
df_rolling['Revenue_Rolling'] = df_rolling['Revenue'].rolling(rolling_window).mean()
df_rolling['GP_Rolling'] = df_rolling['Gross_Profit'].rolling(rolling_window).mean()

fig11 = px.line(df_rolling, x='Date', y=['Revenue_Rolling','GP_Rolling'],
                title=f"{rolling_window}-Month Rolling Averages (Revenue, Gross Profit)")
st.plotly_chart(fig11, use_container_width=True)

# -----------------------------------------------------------------------------
# 12. Altair Interactive Chart (Revenue by Region over Time)
# -----------------------------------------------------------------------------
st.header("12. Altair Interactive Chart (Revenue by Region)")
st.markdown(
    """
    Using **Altair**, create an interactive chart to filter **Revenue** 
    by **Region** over time.
    """
)
brush = alt.selection(type='interval', encodings=['x'])

alt_chart = alt.Chart(data).mark_line().encode(
    x='Date:T',
    y='Revenue:Q',
    color='Region:N'
).add_selection(
    brush
).properties(width=600)

st.altair_chart(alt_chart, use_container_width=True)

# -----------------------------------------------------------------------------
# 13. Boxplot of Monthly Revenue Distribution
# -----------------------------------------------------------------------------
st.header("13. Boxplot of Monthly Revenue")
st.markdown(
    """
    A **boxplot** reveals the distribution, median, and outliers for monthly revenue.
    """
)
fig13 = px.box(data, x='Year', y='Revenue', title="Boxplot: Revenue Distribution by Year")
st.plotly_chart(fig13, use_container_width=True)

# -----------------------------------------------------------------------------
# 14. Month-over-Month Growth Rate
# -----------------------------------------------------------------------------
st.header("14. Month-over-Month Growth Rate")
st.markdown(
    """
    Calculate and visualize the **MoM growth rate** in revenue to measure short-term momentum.
    """
)
data = data.sort_values('Date').reset_index(drop=True)
data['Revenue_MoM_Growth_%'] = data['Revenue'].pct_change() * 100

fig14 = px.bar(data, x='Date', y='Revenue_MoM_Growth_%',
               title="Month-over-Month Revenue Growth (%)")
st.plotly_chart(fig14, use_container_width=True)

# -----------------------------------------------------------------------------
# 15. Treemap of Expense Categories
# -----------------------------------------------------------------------------
st.header("15. Treemap of Expense Categories")
st.markdown(
    """
    A **treemap** can show the proportion of different expense categories at a glance.
    """
)
expense_data = pd.DataFrame({
    'Category': ['COGS', 'Operating_Expenses', 'Marketing_Expenses'],
    'Value': [
        data['COGS'].sum(),
        data['Operating_Expenses'].sum(),
        data['Marketing_Expenses'].sum(),
    ]
})
fig15 = px.treemap(expense_data, path=['Category'], values='Value',
                   title="Expense Categories Treemap")
st.plotly_chart(fig15, use_container_width=True)

# -----------------------------------------------------------------------------
# 16. KPI Cards (Key Performance Indicators)
# -----------------------------------------------------------------------------
st.header("16. KPI Cards")
st.markdown(
    """
    Display current KPIs in a clear, at-a-glance format—such as total revenue, 
    gross margin %, and net income to revenue ratio.
    """
)
total_revenue = data['Revenue'].sum()
avg_gross_margin = (data['Gross_Profit'].sum()/total_revenue)*100
net_income_ratio = (data['Net_Income'].sum()/total_revenue)*100

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Revenue (All Time)", value=f"${total_revenue:,.0f}")
with col2:
    st.metric(label="Average Gross Margin %", value=f"{avg_gross_margin:,.2f}%")
with col3:
    st.metric(label="Net Income / Revenue %", value=f"{net_income_ratio:,.2f}%")

# -----------------------------------------------------------------------------
# 17. Contribution Margin Analysis
# -----------------------------------------------------------------------------
st.header("17. Contribution Margin Analysis")
st.markdown(
    """
    Evaluate contribution margin (Revenue – Variable Costs) across time or product lines 
    to see which segments are most profitable.
    """
)
# For simplicity, assume 60% of COGS is variable
data['Variable_Costs'] = data['COGS'] * 0.6
data['Contribution_Margin'] = data['Revenue'] - data['Variable_Costs']

fig17 = px.line(data, x='Date', y='Contribution_Margin',
                title="Contribution Margin Over Time")
st.plotly_chart(fig17, use_container_width=True)

# -----------------------------------------------------------------------------
# 18. Interactive Table with Drill-Down
# -----------------------------------------------------------------------------
st.header("18. Interactive Table with Drill-Down")
st.markdown(
    """
    A simple **interactive table** allows users to sort, filter, and inspect 
    underlying data for deeper insights.
    """
)
st.dataframe(data)

# -----------------------------------------------------------------------------
# 19. Scenario Analysis (What-If)
# -----------------------------------------------------------------------------
st.header("19. Scenario Analysis (What-If)")
st.markdown(
    """
    Let users quickly adjust assumptions (like **Revenue Growth Rate** or 
    **Operating Expense** changes) to see impact on net income in a **what-if** scenario.
    """
)
st.subheader("Adjust Growth & Expense Levers")
growth_rate = st.slider("Revenue Growth Rate (%)", min_value=0, max_value=30, value=5)
expense_change = st.slider("Operating Expense Change (%)", min_value=0, max_value=30, value=5)

base_revenue = data['Revenue'].iloc[-1]
base_op_exp = data['Operating_Expenses'].iloc[-1]

# Simple scenario model
new_revenue = base_revenue * (1 + growth_rate/100)
new_op_exp = base_op_exp * (1 + expense_change/100)
new_net_income = new_revenue - data['COGS'].iloc[-1] - new_op_exp - data['Marketing_Expenses'].iloc[-1]

st.metric("Projected Revenue", f"${new_revenue:,.0f}")
st.metric("Projected Operating Expenses", f"${new_op_exp:,.0f}")
st.metric("Projected Net Income", f"${new_net_income:,.0f}")

# -----------------------------------------------------------------------------
# 20. Benchmarking vs. Industry Averages
# -----------------------------------------------------------------------------
st.header("20. Benchmarking vs. Industry Averages")
st.markdown(
    """
    Compare your key metrics (like **Revenue Growth**, **Gross Margin**, **Net Income** ratio) 
    against **industry averages** to see how you stack up.
    """
)
# Synthetic "Industry Averages"
industry_gross_margin = 48.0  # percent
industry_net_income_ratio = 12.0  # percent

gross_margin_user = (data['Gross_Profit'].sum() / data['Revenue'].sum()) * 100
net_income_ratio_user = (data['Net_Income'].sum() / data['Revenue'].sum()) * 100

col_a, col_b = st.columns(2)
with col_a:
    difference_gm = gross_margin_user - industry_gross_margin
    st.metric("Gross Margin vs. Industry Avg (%)",
              f"{gross_margin_user:,.2f}%",
              f"{difference_gm:+.2f}% vs. avg")
with col_b:
    difference_nir = net_income_ratio_user - industry_net_income_ratio
    st.metric("Net Income Ratio vs. Industry Avg (%)",
              f"{net_income_ratio_user:,.2f}%",
              f"{difference_nir:+.2f}% vs. avg")

# -----------------------------------------------------------------------------
# Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    **Thank you for exploring "FP&A Data is Beautiful"!**  
    Experiment with these visuals, adapt them to your own data, and discover deeper 
    insights for actionable financial planning and analysis.
    """
)
