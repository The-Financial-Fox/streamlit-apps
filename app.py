import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# App Title
st.title("Excel File Uploader and Advanced Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file
    try:
        df = pd.read_excel(uploaded_file)
        
        # Display Data Preview
        st.write("### Data Preview")
        st.dataframe(df)

        # Show Summary Statistics
        st.write("### Summary Statistics")
        st.write(df.describe())

        # Fancy Visualizations
        st.write("### Fancy Visualizations")

        # Dropdowns for selecting columns
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        if numeric_columns:
            # Correlation Heatmap
            st.write("#### Correlation Heatmap")
            fig, ax = plt.subplots()
            sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

            # Boxplot
            st.write("#### Boxplot")
            box_col = st.selectbox("Select a column for Boxplot", numeric_columns)
            if box_col:
                fig, ax = plt.subplots()
                sns.boxplot(y=df[box_col], ax=ax)
                ax.set_title(f"Boxplot for {box_col}")
                st.pyplot(fig)

            # Histogram
            st.write("#### Histogram")
            hist_col = st.selectbox("Select a column for Histogram", numeric_columns)
            if hist_col:
                fig, ax = plt.subplots()
                sns.histplot(df[hist_col], bins=20, kde=True, ax=ax)
                ax.set_title(f"Histogram for {hist_col}")
                st.pyplot(fig)

            # Interactive Scatter Plot
            st.write("#### Interactive Scatter Plot")
            scatter_x = st.selectbox("X-axis", numeric_columns, index=0)
            scatter_y = st.selectbox("Y-axis", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)
            if scatter_x and scatter_y:
                fig = px.scatter(df, x=scatter_x, y=scatter_y, title=f"{scatter_x} vs {scatter_y}")
                st.plotly_chart(fig)

        else:
            st.warning("No numeric columns available for visualization.")
    
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Awaiting file upload...")
