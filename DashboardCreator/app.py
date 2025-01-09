import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.set_page_config(page_title="Dynamic FP&A Dashboard", layout="wide")
st.title("📊 Dynamic FP&A Dashboard")

# Sidebar: File Upload
st.sidebar.header("Upload Your Datasets")
uploaded_files = st.sidebar.file_uploader(
    "Upload one or more datasets (CSV/Excel)", type=["csv", "xlsx"], accept_multiple_files=True
)

# Function to load datasets
def load_dataset(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)

# Function to identify dataset type
def identify_dataset_type(df):
    if "Revenue" in df.columns and "Expenses" in df.columns:
        return "Financials"
    elif "Headcount" in df.columns:
        return "Headcount"
    elif "Sales" in df.columns:
        return "Sales"
    else:
        return "General"

# Process uploaded files
datasets = {}
if uploaded_files:
    for file in uploaded_files:
        try:
            df = load_dataset(file)
            dataset_type = identify_dataset_type(df)
            datasets[file.name] = {"data": df, "type": dataset_type}
            st.sidebar.success(f"{file.name} loaded as {dataset_type}")
        except Exception as e:
            st.sidebar.error(f"Failed to load {file.name}: {e}")

# If no files uploaded
if not datasets:
    st.warning("Please upload datasets to proceed.")
    st.stop()

# Dataset Selection
selected_file = st.sidebar.selectbox("Select a dataset", options=datasets.keys())
selected_dataset = datasets[selected_file]["data"]
dataset_type = datasets[selected_file]["type"]

# Display Dataset Info
st.subheader(f"Dataset: {selected_file} ({dataset_type})")
if st.checkbox("Show Raw Data"):
    st.write(selected_dataset)

# Visualizations
st.header("Visualizations")

if dataset_type == "Financials":
    # KPIs
    st.subheader("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    with col1:
        total_revenue = selected_dataset['Revenue'].sum() if 'Revenue' in selected_dataset.columns else 0
        st.metric("Total Revenue", f"${total_revenue:,.2f}")
    with col2:
        total_expenses = selected_dataset['Expenses'].sum() if 'Expenses' in selected_dataset.columns else 0
        st.metric("Total Expenses", f"${total_expenses:,.2f}")
    with col3:
        profit_margin = (
            (total_revenue - total_expenses) / total_revenue * 100
            if total_revenue
            else 0
        )
        st.metric("Profit Margin", f"{profit_margin:.2f}%")

    # Bar Plot: Revenue by Category
    if "Category" in selected_dataset.columns:
        fig, ax = plt.subplots()
        sns.barplot(data=selected_dataset, x="Category", y="Revenue", ax=ax)
        ax.set_title("Revenue by Category")
        st.pyplot(fig)

elif dataset_type == "Headcount":
    # KPIs
    st.subheader("Key Headcount Metrics")
    col1, col2 = st.columns(2)
    with col1:
        total_headcount = selected_dataset["Headcount"].sum() if "Headcount" in selected_dataset.columns else 0
        st.metric("Total Headcount", f"{total_headcount}")
    with col2:
        avg_headcount = selected_dataset["Headcount"].mean() if "Headcount" in selected_dataset.columns else 0
        st.metric("Average Headcount", f"{avg_headcount:.2f}")

    # Line Plot: Headcount Over Time
    if "Year" in selected_dataset.columns and "Headcount" in selected_dataset.columns:
        fig, ax = plt.subplots()
        sns.lineplot(data=selected_dataset, x="Year", y="Headcount", marker="o", ax=ax)
        ax.set_title("Headcount Trend Over Years")
        st.pyplot(fig)

elif dataset_type == "Sales":
    # KPIs
    st.subheader("Key Sales Metrics")
    col1, col2 = st.columns(2)
    with col1:
        total_sales = selected_dataset["Sales"].sum() if "Sales" in selected_dataset.columns else 0
        st.metric("Total Sales", f"${total_sales:,.2f}")
    with col2:
        avg_sales = selected_dataset["Sales"].mean() if "Sales" in selected_dataset.columns else 0
        st.metric("Average Sales", f"${avg_sales:.2f}")

    # Scatter Plot: Sales by Region
    if "Region" in selected_dataset.columns and "Sales" in selected_dataset.columns:
        fig, ax = plt.subplots()
        sns.scatterplot(data=selected_dataset, x="Region", y="Sales", ax=ax)
        ax.set_title("Sales by Region")
        st.pyplot(fig)

else:
    st.info("No specific visualizations available for this dataset type.")

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name](https://github.com/your-repo)")
