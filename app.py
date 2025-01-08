import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("Excel File Uploader and Visualizer")

# Instructions
st.write("Upload an Excel file to visualize its content.")

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file
    try:
        df = pd.read_excel(uploaded_file)
        
        # Show dataframe
        st.write("### Data Preview")
        st.dataframe(df)

        # Data Summary
        st.write("### Data Summary")
        st.write(df.describe())

        # Visualization Options
        st.write("### Visualizations")
        
        # Let user select columns to visualize
        columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if not columns:
            st.write("No numerical columns found for visualization.")
        else:
            st.write("Select two numerical columns for scatter plot:")
            x_axis = st.selectbox("X-axis", columns)
            y_axis = st.selectbox("Y-axis", columns)

            if x_axis and y_axis:
                # Create scatter plot
                fig, ax = plt.subplots()
                ax.scatter(df[x_axis], df[y_axis])
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                ax.set_title(f"{x_axis} vs {y_axis}")
                st.pyplot(fig)
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Awaiting file upload...")
