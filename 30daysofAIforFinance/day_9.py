import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Classification Techniques in FP&A"

def day_9_page():
    # Header
    st.title(f"🧠 Day 9: {TITLE}")
    st.write("Welcome to Day 9! Today, we will explore classification techniques and their applications in financial planning and analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Classification?**")
    st.markdown("- **Decision Trees as a Classification Tool.**")
    st.markdown("- **Applications in FP&A: Risk Assessment, Customer Segmentation.**")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 200
    ages = np.random.randint(20, 60, size=num_samples)
    income = np.random.randint(30000, 120000, size=num_samples)
    spending_score = np.random.randint(1, 100, size=num_samples)
    labels = np.where(spending_score > 50, 1, 0)  # 1 = High spender, 0 = Low spender

    df = pd.DataFrame({"Age": ages, "Income": income, "SpendingScore": spending_score, "Label": labels})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Split the Data
    st.header("Train-Test Split")
    st.write("We'll split the dataset into training and testing sets to evaluate the performance of our classification model.")
    X = df[["Age", "Income", "SpendingScore"]]
    y = df["Label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.write(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

    # Fit Decision Tree Classifier
    st.header("Decision Tree Classifier")
    classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # Model Evaluation
    st.header("Model Evaluation")
    st.write("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Low Spender", "High Spender"], yticklabels=["Low Spender", "High Spender"], ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred, target_names=["Low Spender", "High Spender"]))

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can classification models be used for customer segmentation in FP&A?",
        placeholder="Write your thoughts here...",
        key="day9_q1"
    )

    response_2 = st.text_area(
        "2. What are some potential pitfalls of using decision trees for classification?",
        placeholder="Write your examples here...",
        key="day9_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of classification techniques:")
    st.markdown("- [Decision Tree Classifier Basics](https://scikit-learn.org/stable/modules/tree.html)")
    st.markdown("- [Confusion Matrix Explanation](https://en.wikipedia.org/wiki/Confusion_matrix)")
    st.markdown("- [Classification Metrics Overview](https://scikit-learn.org/stable/modules/model_evaluation.html)")

    st.info("Congratulations on completing Day 9! Tomorrow, we'll explore clustering techniques for financial insights.")

if __name__ == "__main__":
    day_9_page()
