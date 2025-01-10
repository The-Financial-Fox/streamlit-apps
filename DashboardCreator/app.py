import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------------------------------------
# Streamlit FP&A Dashboard
# ------------------------------------------------------------
def main():
    # Page Config
    st.set_page_config(
        page_title="FP&A Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("FP&A Dashboard")

    # Sidebar description
    st.sidebar.header("Instructions")
    st.sidebar.write(
        "1. Upload your dataset (CSV or Excel)\n"
        "2. The dashboard and KPIs will update automatically\n"
        "3. Explore different visuals and details"
    )

    # File uploader
    uploaded_file = st.file_uploader(
        "Upload your FP&A dataset (CSV or Excel)", 
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        # Read the file
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return

        st.subheader("Data Preview")
        st.write(df.head())

        # ------------------------------------------------------------
        # Basic Data Checks
        # ------------------------------------------------------------
        # Ensure columns exist before calculations
        required_columns = ["Segment", "Country", "Product", "Discount Band", 
                            "Units Sold", "Manufacturing Price", "Sale Price", 
                            "Gross Sales", "Discounts", "Sales", "COGS", "Profit", 
                            "Date", "Month Number", "Month Name", "Year"]
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            st.warning(
                f"Missing columns in dataset: {', '.join(missing_cols)}.\n"
                f"Please ensure the file has the expected schema."
            )
            return

        # ------------------------------------------------------------
        # KPI Section
        # ------------------------------------------------------------
        # Example calculations (adapt to your data & definitions)
        # Total Revenue: let's assume it's the sum of 'Sales'
        total_revenue = df["Sales"].sum()

        # Profit Margin: sum of profit / sum of sales
        total_profit = df["Profit"].sum()
        profit_margin = (total_profit / total_revenue) * 100 if total_revenue != 0 else 0

        # Year-over-Year Growth (simple approach): 
        # Compare the most recent year to the prior year
        # For demonstration, let's assume "Year" column is in numeric format
        years = sorted(df["Year"].unique())
        yoy_growth = 0
        if len(years) > 1:
            latest_year = years[-1]
            prior_year = years[-2]
            latest_sales = df.loc[df["Year"] == latest_year, "Sales"].sum()
            prior_sales = df.loc[df["Year"] == prior_year, "Sales"].sum()
            yoy_growth = ((latest_sales - prior_sales) / prior_sales) * 100 if prior_sales != 0 else 0

        # Cost Savings: for demonstration, let's assume cost savings come from "Discounts"
        cost_savings = df["Discounts"].sum()

        # Display the four KPIs in a nice layout
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
        with col2:
            st.metric(label="Profit Margin", value=f"{profit_margin:,.2f}%")
        with col3:
            st.metric(label="YoY Growth", value=f"{yoy_growth:,.2f}%")
        with col4:
            st.metric(label="Cost Savings", value=f"${cost_savings:,.2f}")

        st.markdown("---")

        # ------------------------------------------------------------
        # Map Visualization (Plotly)
        # ------------------------------------------------------------
        # We'll group the data by Country and sum the Sales
        country_sales = df.groupby("Country", as_index=False)["Sales"].sum()

        fig_map = px.choropleth(
            country_sales, 
            locations="Country", 
            locationmode="country names",
            color="Sales",
            hover_name="Country", 
            color_continuous_scale=px.colors.sequential.Plasma,
            title="Sales by Country"
        )

        st.subheader("Geographical Sales Map")
        st.plotly_chart(fig_map, use_container_width=True)

        # ------------------------------------------------------------
        # Drill-Down Table
        # ------------------------------------------------------------
        st.subheader("Drill-Down Table")
        st.write(
            "Use the table below to filter and explore the dataset by various dimensions."
        )
        
        # Optional: Let users pick columns to view
        all_columns = df.columns.tolist()
        default_cols = ["Country", "Segment", "Product", "Year", "Sales", "Profit"]
        selected_columns = st.multiselect(
            "Select columns to display",
            all_columns,
            default=default_cols
        )
        
        # Let users filter by country or segment
        unique_countries = df["Country"].unique().tolist()
        selected_country = st.selectbox("Filter by Country (Optional)", ["All"] + unique_countries)

        if selected_country != "All":
            filter_mask = (df["Country"] == selected_country)
        else:
            filter_mask = [True] * len(df)

        # Additional filter by year
        unique_years = df["Year"].unique().tolist()
        selected_year = st.selectbox("Filter by Year (Optional)", ["All"] + list(unique_years))

        if selected_year != "All":
            filter_mask = filter_mask & (df["Year"] == selected_year)

        filtered_data = df.loc[filter_mask, selected_columns]
        st.dataframe(filtered_data, use_container_width=True)

        # ------------------------------------------------------------
        # Waterfall Chart (Plotly)
        # ------------------------------------------------------------
        # Example Waterfall: break down total revenue step-by-step
        # We'll show how each Segment contributes to the total "Sales"
        segment_sales = df.groupby("Segment", as_index=False)["Sales"].sum()

        # Waterfall expects a list of labels and values (positive or negative)
        waterfall_data = []
        total_sales_sum = 0
        for idx, row in segment_sales.iterrows():
            label = row["Segment"]
            value = row["Sales"]
            waterfall_data.append(go.Waterfall(
                x=[label],
                measure=["relative"],
                y=[value],
            ))

        # Combine each measure in one Waterfall figure
        # One approach is to build a single Waterfall trace with list data:
        measure = ["relative"] * len(segment_sales)
        x_vals = segment_sales["Segment"].tolist()
        y_vals = segment_sales["Sales"].tolist()

        waterfall_trace = go.Waterfall(
            name="Segment Breakdown",
            orientation="v",
            measure=measure,
            x=x_vals,
            text=[f"${val:,.0f}" for val in y_vals],
            y=y_vals
        )

        fig_waterfall = go.Figure()
        fig_waterfall.add_trace(waterfall_trace)
        fig_waterfall.update_layout(
            title="Sales Waterfall by Segment",
            waterfallgap=0.5
        )

        st.subheader("Waterfall Chart: Revenue Breakdown")
        st.plotly_chart(fig_waterfall, use_container_width=True)

    else:
        # If no file is uploaded yet
        st.info("Please upload a CSV or Excel file to begin.")

# Run the app
if __name__ == "__main__":
    main()
