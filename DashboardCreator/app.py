import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import openai
import os

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your API key if not using environment variables

def main():
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
        "3. Explore advanced visualizations below the main dashboard"
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
        # KPI Section
        # ------------------------------------------------------------
        total_revenue = df["Sales"].sum() if "Sales" in df.columns else 0
        total_profit = df["Profit"].sum() if "Profit" in df.columns else 0
        profit_margin = (total_profit / total_revenue * 100) if total_revenue else 0
        yoy_growth = 0  # Add your calculation here
        cost_savings = df["Discounts"].sum() if "Discounts" in df.columns else 0

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Revenue", f"${total_revenue:,.2f}")
        with col2:
            st.metric("Profit Margin", f"{profit_margin:.2f}%")
        with col3:
            st.metric("YoY Growth", f"{yoy_growth:.2f}%")
        with col4:
            st.metric("Cost Savings", f"${cost_savings:,.2f}")

        st.markdown("---")

        # ------------------------------------------------------------
        # Map Visualization (Plotly)
        # ------------------------------------------------------------
        if "Country" in df.columns and "Sales" in df.columns:
            st.subheader("Geographical Sales Map")
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
            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.subheader("Geographical Sales Map")
            st.info("Map is unavailable because either 'Country' or 'Sales' column is missing.")

        # ------------------------------------------------------------
        # Drill-Down Table
        # ------------------------------------------------------------
        st.subheader("Drill-Down Table")
        st.write("Use the table below to filter and explore the dataset by various dimensions.")
        
        all_columns = df.columns.tolist()
        default_cols = [col for col in ["Country", "Segment", "Product", "Year", "Sales", "Profit"] if col in all_columns]
        selected_columns = st.multiselect(
            "Select columns to display",
            all_columns,
            default=default_cols
        )
        
        filter_mask = [True] * len(df)
        if "Country" in df.columns:
            unique_countries = df["Country"].unique().tolist()
            selected_country = st.selectbox("Filter by Country (Optional)", ["All"] + unique_countries)
            if selected_country != "All":
                filter_mask = df["Country"] == selected_country
        if "Year" in df.columns:
            unique_years = df["Year"].unique().tolist()
            selected_year = st.selectbox("Filter by Year (Optional)", ["All"] + unique_years)
            if selected_year != "All":
                filter_mask = filter_mask & (df["Year"] == selected_year)

        filtered_data = df.loc[filter_mask, selected_columns]
        st.dataframe(filtered_data, use_container_width=True)

        # ------------------------------------------------------------
        # Advanced Visualization Playground
        # ------------------------------------------------------------
        st.markdown("---")
        st.header("🎨 Advanced Visualization Playground")
        # Existing code for Heatmap, Boxplot, Bar Graph here...
        # Skipping for brevity.

        # ------------------------------------------------------------
        # GenAI Commentary Section
        # ------------------------------------------------------------
        st.markdown("---")
        st.header("🤖 GenAI Commentary")
        st.write("Get expert-level FP&A insights and suggestions from ChatGPT based on your dataset and visualizations.")

        context_input = st.text_area(
            "Provide additional context or ask specific questions for commentary (optional):",
            placeholder="E.g., 'Focus on YoY trends and profitability insights.'"
        )

        if st.button("Generate Commentary"):
            with st.spinner("Generating FP&A Commentary..."):
                try:
                    prompt = f"""
                    You are a Head of FP&A with extensive experience in finance. Analyze the following dataset and its KPIs:
                    - Total Revenue: ${total_revenue:,.2f}
                    - Profit Margin: {profit_margin:.2f}%
                    - Year-over-Year Growth: {yoy_growth:.2f}%
                    - Cost Savings: ${cost_savings:,.2f}

                    The dataset includes these columns: {', '.join(df.columns)}.

                    Insights from the visualizations:
                    - Geographical Sales Map: Summarize sales performance by region.
                    - Drill-Down Table: Identify key dimensions driving profitability.

                    {context_input}

                    Provide commentary with actionable insights and suggest further analyses.
                    """
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are a Head of FP&A with extensive experience in finance."},
                            {"role": "user", "content": prompt},
                        ],
                        max_tokens=300,
                        temperature=0.7,
                    )
                    commentary = response["choices"][0]["message"]["content"].strip()
                    st.subheader("FP&A Commentary")
                    st.write(commentary)
                except Exception as e:
                    st.error(f"Error generating commentary: {e}")

    else:
        st.info("Please upload a CSV or Excel file to begin.")

if __name__ == "__main__":
    main()
