import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
        # Check for required columns, but DO NOT return if missing
        # ------------------------------------------------------------
        expected_cols = [
            "Segment", "Country", "Product", "Discount Band", 
            "Units Sold", "Manufacturing Price", "Sale Price", 
            "Gross Sales", "Discounts", "Sales", "COGS", "Profit", 
            "Date", "Month Number", "Month Name", "Year"
        ]
        missing_cols = [col for col in expected_cols if col not in df.columns]
        if missing_cols:
            st.warning(
                "The following columns are missing and some features may be disabled: "
                f"{', '.join(missing_cols)}."
            )

        # ------------------------------------------------------------
        # KPI Section (conditionally compute KPIs if columns exist)
        # ------------------------------------------------------------
        
        def get_col_sum(data, col_name):
            if col_name in data.columns:
                return data[col_name].sum()
            return 0

        def safe_div(num, den):
            try:
                return num / den if den != 0 else 0
            except:
                return 0

        total_revenue = get_col_sum(df, "Sales")
        total_profit = get_col_sum(df, "Profit")
        cost_savings = get_col_sum(df, "Discounts")
        profit_margin = safe_div(total_profit, total_revenue) * 100

        yoy_growth = 0
        if ("Year" in df.columns) and ("Sales" in df.columns):
            years = sorted(df["Year"].unique())
            if len(years) > 1:
                latest_year = years[-1]
                prior_year = years[-2]
                latest_sales = df.loc[df["Year"] == latest_year, "Sales"].sum()
                prior_sales = df.loc[df["Year"] == prior_year, "Sales"].sum()
                yoy_growth = safe_div((latest_sales - prior_sales), prior_sales) * 100

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}" if "Sales" in df.columns else "N/A")
        with col2:
            st.metric(label="Profit Margin", value=f"{profit_margin:,.2f}%" if "Profit" in df.columns else "N/A")
        with col3:
            st.metric(label="YoY Growth", value=f"{yoy_growth:,.2f}%" if "Year" in df.columns else "N/A")
        with col4:
            st.metric(label="Cost Savings", value=f"${cost_savings:,.2f}" if "Discounts" in df.columns else "N/A")

        st.markdown("---")

        # ------------------------------------------------------------
        # Map Visualization (Plotly)
        # ------------------------------------------------------------
                # ------------------------------------------------------------
        # Advanced Geographical Sales Map (Pydeck)
        # ------------------------------------------------------------
        if "Country" in df.columns and "Sales" in df.columns:
            st.subheader("Geographical Sales Map")

            # Check for latitude and longitude columns
            if "lat" in df.columns and "lon" in df.columns:
                # Pydeck Layer with latitude and longitude
                scatter_layer = pdk.Layer(
                    "ScatterplotLayer",
                    df,
                    get_position=["lon", "lat"],
                    get_color="[Sales / 1000, 0, 200, 140]",
                    get_radius=300,
                    pickable=True,
                )

                # Define map view
                view_state = pdk.ViewState(
                    latitude=df["lat"].mean(),
                    longitude=df["lon"].mean(),
                    zoom=4,
                    pitch=45,
                )

                # Render map
                st.pydeck_chart(
                    pdk.Deck(
                        layers=[scatter_layer],
                        initial_view_state=view_state,
                        map_style="mapbox://styles/mapbox/dark-v10",
                        tooltip={"html": "<b>Sales:</b> {Sales}<br><b>Country:</b> {Country}",
                                 "style": {"color": "white"}},
                    )
                )
            else:
                st.info("Lat/Lon columns not found. Using Country data.")

                # Fallback: Aggregate sales by country and display in choropleth
                country_sales = df.groupby("Country", as_index=False)["Sales"].sum()
                fig_map = px.choropleth(
                    country_sales,
                    locations="Country",
                    locationmode="country names",
                    color="Sales",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Sales by Country",
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
        # Waterfall Chart
        # ------------------------------------------------------------
        if "Segment" in df.columns and "Sales" in df.columns:
            st.subheader("Waterfall Chart: Revenue Breakdown")
            segment_sales = df.groupby("Segment", as_index=False)["Sales"].sum()
            measure = ["relative"] * len(segment_sales)
            waterfall_trace = go.Waterfall(
                name="Segment Breakdown",
                orientation="v",
                measure=measure,
                x=segment_sales["Segment"].tolist(),
                text=[f"${val:,.0f}" for val in segment_sales["Sales"]],
                y=segment_sales["Sales"].tolist()
            )
            fig_waterfall = go.Figure()
            fig_waterfall.add_trace(waterfall_trace)
            fig_waterfall.update_layout(title="Sales Waterfall by Segment", waterfallgap=0.5)
            st.plotly_chart(fig_waterfall, use_container_width=True)
        else:
            st.subheader("Waterfall Chart: Revenue Breakdown")
            st.info("Waterfall chart is unavailable because either 'Segment' or 'Sales' column is missing.")

        # ------------------------------------------------------------
        # Advanced Visualization Playground
        # ------------------------------------------------------------
        st.markdown("---")
        st.header("🎨 Advanced Visualization Playground")
        st.write("Create custom visualizations by selecting chart types, dimensions, and filters.")

        chart_type = st.selectbox("Select Chart Type", ["Heatmap", "Boxplot", "Bar Graph"])
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        cat_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col]) or df[col].dtype.name == "category"]
        date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]

        x_axis = st.selectbox("X-Axis", options=cat_cols + num_cols)
        y_axis = st.selectbox("Y-Axis", options=num_cols if chart_type != "Heatmap" else cat_cols)
        color = st.selectbox("Color Dimension (Optional)", options=[None] + cat_cols + num_cols)

        st.subheader("Apply Filters (Optional)")
        filters = {}
        for col in cat_cols + date_cols:
            unique_vals = df[col].dropna().unique()
            selected_vals = st.multiselect(f"Filter by {col}", options=unique_vals, default=unique_vals)
            filters[col] = selected_vals

        for col, selected_vals in filters.items():
            df = df[df[col].isin(selected_vals)]

        st.subheader("Generated Visualization")
        if chart_type == "Heatmap":
            if color in num_cols:  # Ensure "Color Dimension" is numerical
                heatmap_fig = px.density_heatmap(
                    df, 
                    x=x_axis, 
                    y=y_axis, 
                    z=color, 
                    histfunc="sum", 
                    color_continuous_scale="Viridis",
                    title=f"Heatmap of {color} by {x_axis} and {y_axis}"
                )
                st.plotly_chart(heatmap_fig, use_container_width=True)
            else:
                st.warning(
                    "Heatmap requires a numerical column for the color dimension. "
                    "Please select a valid numerical column for 'Color Dimension (Optional)'."
                )
        elif chart_type == "Boxplot":
            boxplot_fig = px.box(
                df, 
                x=x_axis, 
                y=y_axis, 
                color=color,
                title=f"Boxplot of {y_axis} by {x_axis}"
            )
            st.plotly_chart(boxplot_fig, use_container_width=True)
        elif chart_type == "Bar Graph":
            bar_fig = px.bar(
                df, 
                x=x_axis, 
                y=y_axis, 
                color=color,
                title=f"Bar Graph of {y_axis} by {x_axis}"
            )
            st.plotly_chart(bar_fig, use_container_width=True)
        else:
            st.info("Select a valid chart type.")

    else:
        st.info("Please upload a CSV or Excel file to begin.")

if __name__ == "__main__":
    main()
