import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

TITLE = "Advanced Regression with Gradient Boosting"

def day_12_page():
    # Header
    st.title(f"📈 Day 12: {TITLE}")
    st.write("Welcome to Day 12! Today, we will explore advanced regression techniques using Gradient Boosting, a powerful ensemble learning method.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Gradient Boosting?**")
    st.markdown("- **How Gradient Boosting Improves Regression.**")
    st.markdown("- **Applications in FP&A: Revenue Forecasting, Cost Estimation.**")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 300
    marketing_spend = np.random.randint(1000, 10000, size=num_samples)
    revenue = marketing_spend * 3 + np.random.randn(num_samples) * 5000

    df = pd.DataFrame({"MarketingSpend": marketing_spend, "Revenue": revenue})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Split the Data
    st.header("Train-Test Split")
    st.write("We'll split the dataset into training and testing sets to evaluate the performance of our regression model.")
    X = df[["MarketingSpend"]]
    y = df["Revenue"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.write(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

    # Fit Gradient Boosting Regressor
    st.header("Gradient Boosting Regressor")
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
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
    ax.scatter(X_test, y_test, color="blue", label="Actual Revenue")
    ax.scatter(X_test, y_pred, color="red", label="Predicted Revenue")
    ax.set_title("Gradient Boosting Regression: Actual vs. Predicted")
    ax.set_xlabel("Marketing Spend ($)")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can Gradient Boosting improve accuracy in financial forecasting?",
        placeholder="Write your thoughts here...",
        key="day12_q1"
    )

    response_2 = st.text_area(
        "2. What factors might affect the performance of a Gradient Boosting model?",
        placeholder="Write your examples here...",
        key="day12_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of Gradient Boosting:")
    st.markdown("- [Gradient Boosting Basics](https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting)")
    st.markdown("- [Hyperparameter Tuning Guide](https://towardsdatascience.com/hyperparameter-tuning-in-gradient-boosting-machines-4e2d3b88f8c5)")
    st.markdown("- [R-Squared Explained](https://en.wikipedia.org/wiki/Coefficient_of_determination)")

    st.info("Congratulations on completing Day 12! Tomorrow, we'll dive into time-series forecasting with advanced methods.")

if __name__ == "__main__":
    day_12_page()
