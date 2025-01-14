import streamlit as st
import pandas as pd
import numpy as np
from scipy.optimize import linprog

TITLE = "Optimization Techniques for FP&A"

def day_14_page():
    # Header
    st.title(f"🔧 Day 14: {TITLE}")
    st.write("Welcome to Day 14! Today, we will explore optimization techniques, focusing on Linear Programming for financial decision-making.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Optimization?**")
    st.markdown("- **Linear Programming Basics.**")
    st.markdown("- **Applications in FP&A: Budget Allocation, Resource Optimization.**")

    # Linear Programming Example
    st.header("Linear Programming for Budget Allocation")
    st.write("We'll solve a simple budget allocation problem using Linear Programming.")

    st.markdown("**Problem Statement:**\nA company has $100,000 to allocate across three departments: Marketing, R&D, and Operations. \nEach department has a minimum and maximum requirement, and the goal is to maximize total productivity.")

    # Input Data
    c = [-3, -5, -2]  # Coefficients for productivity (to maximize)
    A = [[1, 1, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]  # Constraints matrix
    b = [100000, -20000, -15000, -10000]  # RHS values for constraints
    bounds = [(20000, 50000), (15000, 40000), (10000, 30000)]  # Bounds for each department

    # Solve Linear Programming Problem
    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

    st.write("Optimization Results:")
    if result.success:
        allocation = result.x
        total_productivity = -result.fun  # Negate since linprog minimizes
        st.write(f"Optimal Allocation:")
        st.write(f"- Marketing: ${allocation[0]:,.2f}")
        st.write(f"- R&D: ${allocation[1]:,.2f}")
        st.write(f"- Operations: ${allocation[2]:,.2f}")
        st.write(f"Total Productivity: {total_productivity:,.2f}")
    else:
        st.write("Optimization failed. Please check the input parameters.")

    # Visualization
    st.header("Visualization")
    labels = ["Marketing", "R&D", "Operations"]
    fig, ax = plt.subplots()
    ax.pie(allocation, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Optimal Budget Allocation")
    st.pyplot(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How can optimization techniques enhance decision-making in FP&A?",
        placeholder="Write your thoughts here...",
        key="day14_q1"
    )

    response_2 = st.text_area(
        "2. What are some real-world challenges of applying linear programming in finance?",
        placeholder="Write your examples here...",
        key="day14_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of optimization:")
    st.markdown("- [Linear Programming Basics](https://en.wikipedia.org/wiki/Linear_programming)")
    st.markdown("- [Scipy linprog Documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)")
    st.markdown("- [Applications of Optimization in Finance](https://www.analyticsvidhya.com/blog/2021/05/introduction-to-linear-programming-and-its-applications/)")

    st.info("Congratulations on completing Day 14! Tomorrow, we'll explore dashboards and KPI tracking for FP&A.")

if __name__ == "__main__":
    day_14_page()
