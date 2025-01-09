import streamlit as st

def run():
    # Day 3 Header
    st.header("Day 3: Conditional Statements and Loops in Python")

    # Introduction Section
    st.write("""
    **Welcome to Day 3!**  
    Today, we'll explore how to use conditional statements and loops to automate decision-making and repetitive tasks in Python.
    
    ### What You’ll Learn:
    - `if`, `elif`, and `else` statements for decision-making
    - `for` and `while` loops for iteration
    - Practical FP&A examples to apply these concepts
    """)

    # Conditional Statements
    st.subheader("1. Conditional Statements")
    st.write("""
    Conditional statements help Python make decisions based on certain conditions.
    
    Syntax:
    ```python
    if condition:
        # Code block
    elif another_condition:
        # Another code block
    else:
        # Code block if none of the above conditions are true
    ```
    Example:
    ```python
    revenue = 10000
    expenses = 8000
    profit = revenue - expenses

    if profit > 0:
        print("The company is profitable!")
    elif profit == 0:
        print("The company broke even.")
    else:
        print("The company is at a loss.")
    ```
    """)

    # Interactive Example: Conditional Statements
    st.subheader("Interactive Exercise: Conditional Statements")
    revenue = st.number_input("Enter revenue ($):", min_value=0, value=10000, step=100)
    expenses = st.number_input("Enter expenses ($):", min_value=0, value=8000, step=100)
    profit = revenue - expenses

    if profit > 0:
        st.success(f"The company is profitable with a profit of ${profit:,.2f}.")
    elif profit == 0:
        st.warning("The company broke even.")
    else:
        st.error(f"The company is at a loss of ${-profit:,.2f}.")

    # Loops
    st.subheader("2. Loops")
    st.write("""
    Loops help automate repetitive tasks in Python.
    
    ### Types of Loops:
    - **`for` loop**: Iterate over a sequence (like a list or range of numbers).
    - **`while` loop**: Repeat as long as a condition is true.

    Example:
    ```python
    # Using a for loop to calculate cumulative revenue
    monthly_revenues = [10000, 12000, 15000]
    total_revenue = 0
    for revenue in monthly_revenues:
        total_revenue += revenue
    print(total_revenue)  # Output: 37000
    ```
    """)

    # Interactive Example: For Loop
    st.subheader("Interactive Exercise: For Loop")
    monthly_revenues = st.text_input("Enter monthly revenues (comma-separated):", "10000, 12000, 15000")
    try:
        revenue_list = list(map(float, monthly_revenues.split(',')))
        cumulative_revenue = 0
        revenue_progression = []

        for month, revenue in enumerate(revenue_list, 1):
            cumulative_revenue += revenue
            revenue_progression.append(cumulative_revenue)

        st.write("### Monthly Revenue Progression:")
        st.write(revenue_progression)

        # Visualization
        st.line_chart(revenue_progression)
    except ValueError:
        st.error("Please enter valid numeric values separated by commas.")

    # Interactive Example: While Loop
    st.subheader("Interactive Exercise: While Loop")
    target_profit = st.number_input("Enter target profit ($):", min_value=0, value=50000, step=1000)
    monthly_profit = st.number_input("Enter expected monthly profit ($):", min_value=0, value=8000, step=1000)

    months = 0
    total_profit = 0
    while total_profit < target_profit:
        months += 1
        total_profit += monthly_profit

    st.write(f"To reach a target profit of ${target_profit:,.2f}, it will take approximately **{months} months**.")

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Great work today! You've learned how to use conditional statements and loops to automate decisions and repetitive tasks.
    
    Tomorrow, we’ll explore **Forecasting Basics for FP&A**, and you will start to see the power of Python for FP&A .
    """)

    # Call to Action
    st.info("📤 Share your exercises and results with the hashtag #30DaysOfPythonFP&A!")
