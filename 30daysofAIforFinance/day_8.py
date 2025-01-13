import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

TITLE = "Predictive Modeling with Linear Regression"

def day_8_page():
    # Header
    st.title(f"📈 Day 8: {TITLE}")
    st.write("Welcome to Day 8! Today, we will explore how to create predictive models using Linear Regression, a fundamental supervised learning technique.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Predictive Modeling?**")
    st.markdown("- **Linear Regression Basics.**")
    st.markdown("- **Applications in FP&A: Forecasting and Budgeting.**")

    # Explanation of Linear Regression
    st.header("Understanding Linear Regression")
    st.write("Linear Regression is a statistical method used to model the relationship between a dependent variable (target) and one or more independent variables (features).")
    st.markdown("### Key Concepts:")
    st.markdown("- **Intercept**: The point where the regression line crosses the y-axis when all independent variables are zero.")
    st.markdown("- **Slope**: Indicates the change in the dependent variable for a unit change in the independent variable.")
    st.markdown("- **Equation**: \( y = \beta_0 + \beta_1 x \), where \( \beta_0 \) is the intercept and \( \beta_1 \) is the slope.")

    st.markdown("Linear Regression assumes a linear relationship between the independent variable(s) and the dependent variable.")

    # Simulate Dataset
    st.header("Dataset Overview")
    np.random.seed(42)
    num_samples = 100
    years_experience = np.random.rand(num_samples) * 10  # Experience in years
    revenue = 5000 + (years_experience * 1000) + (np.random.randn(num_samples) * 5000)  # Revenue with noise
    df = pd.DataFrame({"YearsExperience": years_experience, "Revenue": revenue})

    st.write("Sample Dataset:")
    st.dataframe(df.head())

    # Split the Data
    st.header("Train-Test Split")
    st.write("We'll split the dataset into training and testing sets to evaluate the performance of our predictive model.")
    X = df[["YearsExperience"]]
    y = df["Revenue"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    st.write(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

    # Fit Linear Regression Model
    st.header("Linear Regression Model")
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.write("Model Coefficients:")
    st.write(f"Intercept: {model.intercept_:.2f}")
    st.write(f"Slope: {model.coef_[0]:.2f}")

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
    ax.plot(X_test, y_pred, color="red", label="Predicted Revenue")
    ax.set_title("Linear Regression: Actual vs. Predicted")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Revenue ($)")
    ax.legend()
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can predictive models improve financial planning processes?",
        placeholder="Write your thoughts here...",
        key="day8_q1"
    )

    response_2 = st.text_area(
        "2. What are the potential limitations of linear regression in financial modeling?",
        placeholder="Write your examples here...",
        key="day8_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of predictive modeling:")
    st.markdown("- [Linear Regression Basics](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86)")
    st.markdown("- [Train-Test Split Explanation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation)")
    st.markdown("- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)")

    st.info("Congratulations on completing Day 8! Tomorrow, we'll explore classification techniques for financial applications.")

if __name__ == "__main__":
    day_8_page()
