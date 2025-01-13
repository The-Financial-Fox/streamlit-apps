import streamlit as st

TITLE = "Basics of Machine Learning"

def day_3_page():
    # Header
    st.title(f"🤖 Day 3: {TITLE}")
    st.write("Welcome to Day 3! Today, we will dive into the fundamentals of Machine Learning (ML) and explore its key concepts.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Machine Learning?**")
    st.markdown("- **Types of ML: Supervised, Unsupervised, and Reinforcement Learning**")
    st.markdown("- **Applications of ML in FP&A:** Revenue Prediction, Expense Classification, and Anomaly Detection.")

    # ML Concepts Explanation
    st.header("Machine Learning Basics")
    st.write("Machine Learning is a subset of AI that enables systems to learn from data and improve their performance without being explicitly programmed.")

    st.subheader("Supervised Learning")
    st.write("Supervised learning involves training a model on labeled data, such as predicting revenue based on historical data.")
    st.markdown("Examples: Linear Regression, Decision Trees, Support Vector Machines")

    st.subheader("Unsupervised Learning")
    st.write("Unsupervised learning involves finding patterns in data without labeled outcomes, such as grouping customers into segments.")
    st.markdown("Examples: K-Means Clustering, Principal Component Analysis")

    st.subheader("Reinforcement Learning")
    st.write("Reinforcement learning involves training models to make sequences of decisions, rewarding positive outcomes.")
    st.markdown("Examples: Game Playing AI, Dynamic Pricing")

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the task:")

    response_1 = st.text_area(
        "1. Can you think of examples where supervised learning could improve FP&A processes?",
        placeholder="Write your thoughts here...",
        key="day3_q1"
    )

    response_2 = st.text_area(
        "2. What potential applications can you identify for unsupervised learning in finance?",
        placeholder="Write your examples here...",
        key="day3_q2"
    )

    st.markdown("3. Train a simple linear regression model with this sample code:")
    st.code(
        """
        import numpy as np
        from sklearn.linear_model import LinearRegression

        # Sample Data
        X = np.array([[1], [2], [3], [4], [5]])  # Features
        y = np.array([100, 200, 300, 400, 500])  # Targets

        # Create and train the model
        model = LinearRegression()
        model.fit(X, y)

        # Make predictions
        predictions = model.predict(X)
        print(predictions)
        """,
        language="python"
    )

    st.markdown("Run the code in your Python environment to see a simple ML model in action.")

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of Machine Learning:")
    st.markdown("- [Introduction to Machine Learning](https://www.ibm.com/cloud/learn/machine-learning)")
    st.markdown("- [Scikit-Learn Documentation](https://scikit-learn.org/stable/documentation.html)")
    st.markdown("- [Machine Learning in Finance](https://www.forbes.com/sites/forbestechcouncil/2021/05/14/ai-in-finance/)")

    st.info("Congratulations on completing Day 3! Tomorrow, we'll dive into time-series analysis for FP&A.")

if __name__ == "__main__":
    day_3_page()
