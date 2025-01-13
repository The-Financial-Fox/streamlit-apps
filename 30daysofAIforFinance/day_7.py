import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Data Preparation and Dimensionality Reduction"

def day_7_page():
    # Header
    st.title(f"📉 Day 7: {TITLE}")
    st.write("Welcome to Day 7! Today, we will learn about data preparation and how dimensionality reduction techniques like PCA can simplify complex datasets.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **Why is Data Preparation Important?**")
    st.markdown("- **Steps in Data Cleaning and Transformation.**")
    st.markdown("- **Dimensionality Reduction using PCA.**")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 100
    features = ["Revenue", "Expenses", "Profit", "Growth", "Market Share"]
    data = np.random.rand(num_samples, len(features)) * 1000
    df = pd.DataFrame(data, columns=features)

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Standardize the Data
    st.header("Data Standardization")
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    st.write("Standardized Data (first 5 rows):")
    st.dataframe(pd.DataFrame(scaled_data, columns=features).head())

    # PCA Section
    st.header("Dimensionality Reduction with PCA")
    st.write("Principal Component Analysis (PCA) is used to reduce the dimensionality of data while retaining most of its variance.")

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    explained_variance = pca.explained_variance_ratio_

    st.write("Explained Variance by Components:")
    st.bar_chart(pd.DataFrame({"Component": ["PC1", "PC2"], "Explained Variance": explained_variance}))

    # Visualize PCA Results
    pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
    fig, ax = plt.subplots()
    sns.scatterplot(x=pca_df["PC1"], y=pca_df["PC2"], alpha=0.7, ax=ax)
    ax.set_title("PCA Result: Data in Reduced Dimensions")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. Why is it important to standardize data before applying PCA?",
        placeholder="Write your thoughts here...",
        key="day7_q1"
    )

    response_2 = st.text_area(
        "2. What insights can dimensionality reduction provide in financial datasets?",
        placeholder="Write your examples here...",
        key="day7_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of data preparation and PCA:")
    st.markdown("- [Understanding PCA](https://towardsdatascience.com/a-quick-introduction-to-principal-component-analysis-772533a1e6a3)")
    st.markdown("- [Scikit-Learn PCA Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)")
    st.markdown("- [StandardScaler Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)")

    st.info("Congratulations on completing Day 7! Tomorrow, we'll dive deeper into advanced predictive modeling.")

if __name__ == "__main__":
    day_7_page()
