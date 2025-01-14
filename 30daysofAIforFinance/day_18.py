import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

TITLE = "Advanced Forecasting with Machine Learning"

def day_18_page():
    # Header
    st.title(f"🤖 Day 18: {TITLE}")
    st.write("Welcome to Day 18! Today, we will explore advanced forecasting techniques using machine learning, specifically Random Forest Regression.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Random Forest Regression?**")
    st.markdown("- **How Machine Learning Enhances Forecasting.**")
    st.markdown("- **Applications in FP&A: Predicting Revenue, Costs, and Demand.**")

    # Simulated Dataset
    st.header("Simulated Dataset")
    np.random.seed(42)
    num_samples = 500
    marketing_spend = np.random.randint(1000, 10000, size=num_samples)
    product_price = np.random.uniform(20, 100, size=num_samples)
    revenue = (marketing_spend * 0.1 + product_price * 50 + np.random.randn(num_samples) * 500)

    df = pd.DataFrame({
        "MarketingSpend": marketing_spend,
        "ProductPrice": product_price,
        "Revenue": revenue
    })

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Train-Test Split
    st.header("Train-Test Split")
    st.write("We'll split the dataset into training and testing sets to evaluate the performance of our Random Forest model.")
    X = df[["MarketingSpend", "ProductPrice"]]
    y = df["Revenue"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.write(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

    # Random Forest Regression
    st.header("Random Forest Regression")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Model Evaluation
    st.header("Model Evaluation")
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    st.write(f"Mean Squared Error: {mse:.2f}")
    st.write(f"R-Squared: {r2:.2f}")

    # Visualization
    st.header("Visualization")
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, alpha=0.7, color="blue")
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red", linestyle="--")
    ax.set_title("Actual vs. Predicted Revenue")
    ax.set_xlabel("Actual Revenue ($)")
    ax.set_ylabel("Predicted Revenue ($)")
    st.pyplot(fig)

    # Feature Importance
    st.header("Feature Importance")
    feature_importance = pd.DataFrame({
        "Feature": ["MarketingSpend", "ProductPrice"],
        "Importance": model.feature_importances_
    }).sort_values(by="Importance", ascending=False)

    st.write(feature_importance)

    fig, ax = plt.subplots()
    sns.barplot(x="Importance", y="Feature", data=feature_importance, palette="coolwarm", ax=ax)
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can Random Forest improve revenue forecasting in FP&A?",
        placeholder="Write your thoughts here...",
        key="day18_q1"
    )

    response_2 = st.text_area(
        "2. What other features could enhance the accuracy of this forecasting model?",
        placeholder="Write your examples here...",
        key="day18_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of machine learning forecasting techniques:")
    st.markdown("- [Random Forest Regression Basics](https://scikit-learn.org/stable/modules/ensemble.html#forest)")
    st.markdown("- [Feature Importance in Machine Learning](https://machinelearningmastery.com/calculate-feature-importance-with-python/)")
    st.markdown("- [Advanced Forecasting Techniques](https://towardsdatascience.com/machine-learning-for-forecasting-6d787785496c)")

    st.info("Congratulations on completing Day 18! Tomorrow, we'll explore cost allocation techniques.")

if __name__ == "__main__":
    day_18_page()
