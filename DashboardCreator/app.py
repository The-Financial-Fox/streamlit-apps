import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App Title
st.set_page_config(page_title="Dynamic FP&A Dashboard", layout="wide")
st.title("📊 Dynamic FP&A Dashboard")

# Sidebar: File Upload
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader(
    "Upload a CSV or Excel file", type=["csv", "xlsx"]
)

# Load Dataset
if uploaded_file:
    # Load the file
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error("Error loading file. Please check the format.")
        st.stop()

    # Display dataset
    st.subheader("Uploaded Dataset")
    if st.checkbox("Show Raw Data"):
        st.write(data)

    # Sidebar: Select columns
    st.sidebar.header("Visualization Options")
    st.sidebar.subheader("Select Columns")
    x_col = st.sidebar.selectbox("Select X-Axis Column", options=data.columns)
    y_col = st.sidebar.selectbox("Select Y-Axis Column", options=data.columns)

    # Sidebar: Select Graph Type
    st.sidebar.subheader("Select Graph Type")
    graph_type = st.sidebar.selectbox(
        "Choose Graph Type",
        [
            "Line Chart",
            "Bar Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Pie Chart",
            "Heatmap",
            "Area Chart",
            "KDE Plot",
            "Violin Plot",
        ],
    )

    # Generate Graphs
    st.header("Visualization")

    # Handle different graph types
    try:
        if graph_type == "Line Chart":
            fig, ax = plt.subplots()
            sns.lineplot(data=data, x=x_col, y=y_col, ax=ax)
            ax.set_title(f"Line Chart: {y_col} vs {x_col}")
            st.pyplot(fig)

        elif graph_type == "Bar Chart":
            fig, ax = plt.subplots()
            sns.barplot(data=data, x=x_col, y=y_col, ax=ax)
            ax.set_title(f"Bar Chart: {y_col} vs {x_col}")
            st.pyplot(fig)

        elif graph_type == "Scatter Plot":
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=x_col, y=y_col, ax=ax)
            ax.set_title(f"Scatter Plot: {y_col} vs {x_col}")
            st.pyplot(fig)

        elif graph_type == "Histogram":
            fig, ax = plt.subplots()
            sns.histplot(data=data[x_col], bins=20, kde=True, ax=ax)
            ax.set_title(f"Histogram: {x_col}")
            st.pyplot(fig)

        elif graph_type == "Box Plot":
            fig, ax = plt.subplots()
            sns.boxplot(data=data, x=x_col, y=y_col, ax=ax)
            ax.set_title(f"Box Plot: {y_col} by {x_col}")
            st.pyplot(fig)

        elif graph_type == "Pie Chart":
            if data[x_col].nunique() <= 10:  # Limit pie charts to 10 unique categories
                pie_data = data[x_col].value_counts()
                fig, ax = plt.subplots()
                ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
                ax.set_title(f"Pie Chart: Distribution of {x_col}")
                st.pyplot(fig)
            else:
                st.warning("Pie charts are limited to columns with 10 or fewer unique values.")

        elif graph_type == "Heatmap":
            if data.select_dtypes(include="number").shape[1] > 1:  # Ensure numeric columns are available
                fig, ax = plt.subplots()
                sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
                ax.set_title("Heatmap: Correlation Matrix")
                st.pyplot(fig)
            else:
                st.warning("Heatmaps require at least two numeric columns.")

        elif graph_type == "Area Chart":
            fig, ax = plt.subplots()
            data.sort_values(x_col, inplace=True)
            ax.fill_between(data[x_col], data[y_col], alpha=0.5)
            ax.set_title(f"Area Chart: {y_col} vs {x_col}")
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)

        elif graph_type == "KDE Plot":
            fig, ax = plt.subplots()
            sns.kdeplot(data=data, x=x_col, ax=ax)
            ax.set_title(f"KDE Plot: Distribution of {x_col}")
            st.pyplot(fig)

        elif graph_type == "Violin Plot":
            fig, ax = plt.subplots()
            sns.violinplot(data=data, x=x_col, y=y_col, ax=ax)
            ax.set_title(f"Violin Plot: {y_col} by {x_col}")
            st.pyplot(fig)

        else:
            st.warning("Invalid graph type selected.")

    except Exception as e:
        st.error(f"Error generating graph: {e}")

else:
    st.warning("Please upload a dataset to get started.")

# Footer
st.markdown("---")
st.markdown("Developed by [Christian Martinez](https://github.com/your-repo)")
