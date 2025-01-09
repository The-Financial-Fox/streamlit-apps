import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run():
    # Day 1 Header
    st.header("Day 1: Introduction to Python for FP&A")

    # Introduction Section
    st.write("""
    **Welcome to Day 1!**  
    Today, we'll cover the basics of Python and understand how it applies to Financial Planning and Analysis (FP&A).
    
    ### What You’ll Learn:
    - Why Python is valuable for FP&A.
    - Setting up your Python environment.
    - Writing your first Python script.
    """)

    # Why Python for FP&A
    st.subheader("Why Python for FP&A?")
    st.write("""
    Python is an essential tool for FP&A professionals due to:
    - **Automation**: Replace manual tasks with automated scripts.
    - **Data Analysis**: Efficiently analyze large datasets.
    - **Visualization**: Create insightful and professional visualizations.
    - **Scalability**: Handle growing complexities in financial data.
    """)

    # Visual: Python Usage in FP&A
    st.image(
        "https://miro.medium.com/max/700/1*3N0hpX_vTm8opGt5rZeV9Q.png",
        caption="Python Use Cases in FP&A",
    )

    # Getting Started with Python
    st.subheader("Getting Started")
    st.write("""
    Follow these steps to set up Python:
    1. Download and install [Python](https://www.python.org/downloads/).
    2. Install an IDE like [VS Code](https://code.visualstudio.com/) or [Jupyter Notebook](https://jupyter.org/).
    3. Install `pip` for package management.
    4. Install Streamlit:  
       ```bash
       pip install streamlit
       ```
    """)

    # Example Mini-Project: Monthly Revenue Growth
    st.subheader("Example: Calculate Monthly Revenue Growth")
    st.write("Use Python to calculate monthly revenue growth based on sample data:")
    st.code("""
revenue = [10000, 12000, 15000]
growth_rate = [(revenue[i] - revenue[i-1]) / revenue[i-1] * 100 for i in range(1, len(revenue))]
print(growth_rate)  # Output: [20.0, 25.0]
    """)

    # Interactive Exercise: Calculate Growth
    st.subheader("Interactive Exercise")
    st.write("Modify the revenue data below and calculate the growth rate.")
    
    # Input for Revenue
    revenue_data = st.text_input("Enter revenue data (comma-separated):", "10000, 12000, 15000")
    try:
        revenue = list(map(float, revenue_data.split(',')))
        growth_rate = [(revenue[i] - revenue[i-1]) / revenue[i-1] * 100 for i in range(1, len(revenue))]

        # Display Results
        st.write("### Growth Rates (%):")
        st.write(growth_rate)

        # Plot Results
        fig, ax = plt.subplots()
        ax.plot(range(1, len(growth_rate)+1), growth_rate, marker='o')
        ax.set_title("Monthly Revenue Growth")
        ax.set_xlabel("Month")
        ax.set_ylabel("Growth Rate (%)")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Invalid input: {e}")

    # Wrap-Up
    st.subheader("Wrap-Up")
    st.write("""
    Congratulations on completing Day 1!  
    Tomorrow, we’ll dive deeper into Python fundamentals and explore FP&A-specific use cases.  
    Stay consistent, and don’t hesitate to reach out to the community for help.
    """)

    # Call to Action
    st.info("📤 Share your progress on social media with #30DaysOfPythonFP&A!")
