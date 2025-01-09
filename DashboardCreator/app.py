import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.set_page_config(page_title="FP&A Dashboard", layout="wide")
st.title("📊 FP&A Dashboard")

# Sidebar: File Upload and Year Filter
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
year_filter = st.sidebar.selectbox("Select a Year", options=[])

if uploaded_file:
    # Read Data
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error("Error reading file. Please check the format.")
        st.stop()

    st.sidebar.success("File uploaded successfully!")
    
    # Display Dataset
    if st.checkbox("Show Raw Data"):
        st.write(data)

    # Add Year Options
    if 'Year' in data.columns:
        year_filter = st.sidebar.selectbox("Select a Year", options=data['Year'].unique())
        filtered_data = data[data['Year'] == year_filter]
    else:
        st.warning("No 'Year' column found in dataset.")
        filtered_data = data

    # KPIs Section
    st.header("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    with col1:
        total_revenue = filtered_data['Revenue'].sum() if 'Revenue' in filtered_data.columns else 0
        st.metric("Total Revenue", f"${total_revenue:,.2f}")
    with col2:
        total_expenses = filtered_data['Expenses'].sum() if 'Expenses' in filtered_data.columns else 0
        st.metric("Total Expenses", f"${total_expenses:,.2f}")
    with col3:
        profit_margin = (total_revenue - total_expenses) / total_revenue * 100 if total_revenue else 0
        st.metric("Profit Margin", f"{profit_margin:.2f}%")

    # Visualizations
    st.header("Visualizations")
    if 'Category' in filtered_data.columns and 'Revenue' in filtered_data.columns:
        fig, ax = plt.subplots()
        sns.barplot(data=filtered_data, x='Category', y='Revenue', ax=ax)
        ax.set_title("Revenue by Category")
        st.pyplot(fig)

    if 'Month' in filtered_data.columns and 'Expenses' in filtered_data.columns:
        fig, ax = plt.subplots()
        sns.lineplot(data=filtered_data, x='Month', y='Expenses', marker="o", ax=ax)
        ax.set_title("Monthly Expenses Trend")
        st.pyplot(fig)

else:
    st.warning("Please upload a dataset to proceed.")

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name](https://github.com/your-repo)")
