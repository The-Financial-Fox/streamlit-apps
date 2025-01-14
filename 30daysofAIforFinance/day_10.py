import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Clustering Techniques in FP&A"

def day_10_page():
    # Header
    st.title(f"🔍 Day 10: {TITLE}")
    st.write("Welcome to Day 10! Today, we will explore clustering techniques and their applications in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Clustering?**")
    st.markdown("- **K-Means Clustering Basics.**")
    st.markdown("- **Applications in FP&A: Customer Segmentation, Expense Categorization.**")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 300
    age = np.random.randint(20, 60, size=num_samples)
    income = np.random.randint(30000, 120000, size=num_samples)
    spending_score = np.random.randint(1, 100, size=num_samples)

    df = pd.DataFrame({"Age": age, "Income": income, "SpendingScore": spending_score})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # K-Means Clustering
    st.header("K-Means Clustering")
    st.write("K-Means is a popular clustering algorithm used to group data points into a predefined number of clusters.")

    # Select number of clusters
    num_clusters = st.slider("Select the number of clusters (K):", min_value=2, max_value=10, value=3)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df)

    # Cluster Centers
    st.write("Cluster Centers:")
    st.dataframe(pd.DataFrame(kmeans.cluster_centers_, columns=["Age", "Income", "SpendingScore"]))

    # Visualize Clusters
    st.header("Cluster Visualization")
    fig, ax = plt.subplots()
    sns.scatterplot(
        x="Income", y="SpendingScore", hue="Cluster", palette="tab10", data=df, ax=ax, s=100
    )
    ax.set_title("Customer Segments Based on Income and Spending Score")
    ax.set_xlabel("Income ($)")
    ax.set_ylabel("Spending Score")
    ax.legend(title="Cluster")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can clustering techniques help in identifying customer segments?",
        placeholder="Write your thoughts here...",
        key="day10_q1"
    )

    response_2 = st.text_area(
        "2. What are some challenges in choosing the right number of clusters for K-Means?",
        placeholder="Write your examples here...",
        key="day10_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of clustering techniques:")
    st.markdown("- [K-Means Clustering Basics](https://scikit-learn.org/stable/modules/clustering.html#k-means)")
    st.markdown("- [Elbow Method for Choosing K](https://en.wikipedia.org/wiki/Elbow_method_(clustering))")
    st.markdown("- [Seaborn Visualization Documentation](https://seaborn.pydata.org/)")

    st.info("Congratulations on completing Day 10! Tomorrow, we'll dive into more advanced analytics techniques.")

if __name__ == "__main__":
    day_10_page()
