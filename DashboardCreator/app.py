import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def main():
    st.set_page_config(
        page_title="FP&A Dashboard",
        layout="wide",
        initial_sidebar_state="collapsed"
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
        # Advanced Visualization Playground
        # ------------------------------------------------------------
        st.markdown("---")
        st.header("🎨 Advanced Visualization Playground")
        st.write("Create custom visualizations by selecting chart types, dimensions, and filters.")

        # Visualization Type Selection
        chart_type = st.selectbox(
            "Select Chart Type", 
            ["Heatmap", "Boxplot", "Bar Graph"]
        )

        # Filter by columns
        st.subheader("Customize Dimensions")
        num_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
        cat_cols = [col for col in df.columns if pd.api.types.is_string_dtype(df[col]) or df[col].dtype.name == "category"]
        date_cols = [col for col in df.columns if pd.api.types.is_datetime64_any_dtype(df[col])]

        # Axis selection
        x_axis = st.selectbox("X-Axis", options=cat_cols + num_cols)
        y_axis = st.selectbox("Y-Axis", options=num_cols if chart_type != "Heatmap" else cat_cols)
        color = st.selectbox("Color Dimension (Optional)", options=[None] + cat_cols)

        # Apply Filters
        st.subheader("Apply Filters (Optional)")
        filters = {}
        for col in cat_cols + date_cols:
            unique_vals = df[col].dropna().unique()
            selected_vals = st.multiselect(f"Filter by {col}", options=unique_vals, default=unique_vals)
            filters[col] = selected_vals

        # Filter the dataframe based on user selection
        for col, selected_vals in filters.items():
            df = df[df[col].isin(selected_vals)]

        # ------------------------------------------------------------
        # Generate Visualizations
        # ------------------------------------------------------------
        st.subheader("Generated Visualization")
        if chart_type == "Heatmap":
            # Generate a heatmap (requires x and y to be categorical, and color to be numerical)
            if color in num_cols:
                heatmap_fig = px.density_heatmap(
                    df, x=x_axis, y=y_axis, z=color, histfunc="sum",
                    color_continuous_scale="Viridis",
                    title=f"Heatmap of {color} by {x_axis} and {y_axis}"
                )
                st.plotly_chart(heatmap_fig, use_container_width=True)
            else:
                st.warning("Heatmap requires a numerical column for the color dimension.")

        elif chart_type == "Boxplot":
            # Generate a boxplot
            boxplot_fig = px.box(
                df, x=x_axis, y=y_axis, color=color,
                title=f"Boxplot of {y_axis} by {x_axis}",
                points="all"
            )
            st.plotly_chart(boxplot_fig, use_container_width=True)

        elif chart_type == "Bar Graph":
            # Generate a bar graph
            bar_fig = px.bar(
                df, x=x_axis, y=y_axis, color=color,
                title=f"Bar Graph of {y_axis} by {x_axis}"
            )
            st.plotly_chart(bar_fig, use_container_width=True)
        else:
            st.info("Select a chart type to get started.")

    else:
        st.info("Please upload a CSV or Excel file to begin.")

if __name__ == "__main__":
    main()
