import streamlit as st
import matplotlib.pyplot as plt

def run():
    # Day 2 Header
    st.header("Day 2: Python Fundamentals for FP&A")
    
    # Introduction Section
    st.write("""
    **Welcome to Day 2!**  
    Today, we'll explore the fundamental building blocks of Python, including:
    - Variables
    - Data types
    - Basic mathematical operations

    These are essential for creating financial models and performing calculations in FP&A.
    """)

    # Variables and Data Types
    st.subheader("1. Variables and Data Types")
    st.write("""
    In Python, variables are used to store data. Here are some common data types:
    - **Integer (`int`)**: Whole numbers like 1, 2, 100
    - **Float (`float`)**: Decimal numbers like 1.5, 2.7, 100.0
    - **String (`str`)**: Text like "Revenue" or "Hello World"
    - **Boolean (`bool`)**: True or False
    
    Example:
    ```python
    revenue = 10000        # Integer
    growth_rate = 0.15     # Float
    company_name = "XYZ"   # String
    is_profitable = True   # Boolean
    ```
    """)
    
    # Interactive Exercise: Define Variables
    st.subheader("Interactive Exercise: Define Variables")
    company_name = st.text_input("Enter a company name:", "ABC Corp")
    revenue = st.number_input("Enter the company's revenue ($):", min_value=0, value=10000, step=100)
    growth_rate = st.slider("Select the expected growth rate (%):", min_value=0.0, max_value=100.0, value=15.0, step=0.1)
    is_profitable = st.radio("Is the company profitable?", ["Yes", "No"]) == "Yes"

    # Display Inputs
    st.write(f"### Company Overview")
    st.write(f"- **Name:** {company_name}")
    st.write(f"- **Revenue:** ${revenue:,.2f}")
    st.write(f"- **Growth Rate:** {growth_rate:.1f}%")
    st.write(f"- **Profitable:** {'Yes' if is_profitable else 'No'}")

    # Basic Operations
    st.subheader("2. Basic Mathematical Operations")
    st.write("""
    Python can handle basic math operations like addition, subtraction, multiplication, and division:
    ```python
    # Example
    revenue = 10000
    expenses = 7000
    profit = revenue - expenses
    print(profit)  # Output: 3000
    ```
    """)
    
    # Interactive Exercise: Calculate Profit
    st.subheader("Interactive Exercise: Calculate Profit")
    expenses = st.number_input("Enter the company's expenses ($):", min_value=0, value=7000, step=100)
    profit = revenue - expenses
    st.write(f"**Profit:** ${profit:,.2f}")

    # Visualization: Profit Breakdown
    st.subheader("Profit Breakdown")
    fig, ax = plt.subplots()
    labels = ['Revenue', 'Expenses', 'Profit']
    values = [revenue, expenses, profit]
    colors = ['#76C1FA', '#FA8072', '#90EE90']

    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
    st.pyplot(fig)

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Great work! Today, you learned about variables, data types, and basic operations in Python.  
    These foundational concepts are critical for building financial models and performing FP&A tasks.  

    Tomorrow, we'll dive into conditional statements and loops, which are essential for decision-making and automation.
    """)

    # Call to Action
    st.info("📤 Share your results and insights on social media using #30DaysOfPythonFP&A!")
