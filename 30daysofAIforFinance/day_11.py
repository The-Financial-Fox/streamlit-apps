import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Advanced Classification with Random Forest"

def day_11_page():
    # Header
    st.title(f"🌳 Day 11: {TITLE}")
    st.write("Welcome to Day 11! Today, we will explore advanced classification techniques using Random Forest, a powerful ensemble learning method.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Random Forest?**")
    st.markdown("- **How Random Forest Improves Classification.**")
    st.markdown("- **Applications in FP&A: Fraud Detection, Risk Assessment.**")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 500
    age = np.random.randint(20, 60, size=num_samples)
    income = np.random.randint(30000, 120000, size=num_samples)
    credit_score = np.random.randint(300, 850, size=num_samples)
    labels = np.where((credit_score > 600) & (income > 50000), 1, 0)  # 1 = Good Credit, 0 = Poor Credit

    df = pd.DataFrame({"Age": age, "Income": income, "CreditScore": credit_score, "Label": labels})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Split the Data
    st.header("Train-Test Split")
    st.write("We'll split the dataset into training and testing sets to evaluate the performance of our classification model.")
    X = df[["Age", "Income", "CreditScore"]]
    y = df["Label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.write(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

    # Fit Random Forest Classifier
    st.header("Random Forest Classifier")
    classifier = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    # Model Evaluation
    st.header("Model Evaluation")
    st.write("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Poor Credit", "Good Credit"], yticklabels=["Poor Credit", "Good Credit"], ax=ax)
    ax.set_title("Confusion Matrix")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)

    st.write("Classification Report:")
    st.text(classification_report(y_test, y_pred, target_names=["Poor Credit", "Good Credit"]))

    # Feature Importance
    st.header("Feature Importance")
    feature_importance = pd.DataFrame({
        "Feature": ["Age", "Income", "CreditScore"],
        "Importance": classifier.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    st.write(feature_importance)

    fig, ax = plt.subplots()
    sns.barplot(x="Importance", y="Feature", data=feature_importance, palette="viridis", ax=ax)
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can Random Forest improve classification accuracy in FP&A applications?",
        placeholder="Write your thoughts here...",
        key="day11_q1"
    )

    response_2 = st.text_area(
        "2. Why is feature importance valuable when interpreting classification models?",
        placeholder="Write your examples here...",
        key="day11_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of Random Forest:")
    st.markdown("- [Random Forest Basics](https://scikit-learn.org/stable/modules/ensemble.html#forest)")
    st.markdown("- [Feature Importance Explanation](https://machinelearningmastery.com/calculate-feature-importance-with-python/)")
    st.markdown("- [Confusion Matrix Guide](https://en.wikipedia.org/wiki/Confusion_matrix)")

    st.info("Congratulations on completing Day 11! Tomorrow, we'll explore regression techniques for predictive modeling.")

if __name__ == "__main__":
    day_11_page()
