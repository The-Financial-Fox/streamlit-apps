import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

TITLE = "Cost Allocation Techniques in FP&A"

def day_19_page():
    # Header
    st.title(f"💰 Day 19: {TITLE}")
    st.write("Welcome to Day 19! Today, we will explore cost allocation techniques, focusing on distributing shared costs among business units or projects.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Cost Allocation?**")
    st.markdown("- **Methods for Allocating Costs: Direct, Step-Down, and Activity-Based.**")
    st.markdown("- **Applications in FP&A: Profitability Analysis, Budget Planning.**")

    # Simulated Cost Allocation Data
    st.header("Simulated Cost Allocation Data")
    np.random.seed(42)
    units = ["Unit A", "Unit B", "Unit C"]
    direct_costs = np.random.randint(20000, 50000, size=3)
    shared_costs = 30000
    allocation_keys = np.random.uniform(0.2, 0.5, size=3)
    allocation_keys /= allocation_keys.sum()  # Normalize to sum to 1

    shared_allocation = shared_costs * allocation_keys
    total_costs = direct_costs + shared_allocation

    df = pd.DataFrame({
        "Unit": units,
        "Direct Costs": direct_costs,
        "Shared Costs Allocated": shared_allocation,
        "Total Costs": total_costs
    })

    st.write("Cost Allocation Table:")
    st.dataframe(df)

    # Visualization
    st.header("Visualization")
    fig = px.bar(df, x="Unit", y=["Direct Costs", "Shared Costs Allocated"],
                 title="Cost Allocation Breakdown",
                 labels={"value": "Cost ($)", "Unit": "Business Unit"},
                 barmode="stack")
    st.plotly_chart(fig)

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and complete the tasks:")

    response_1 = st.text_area(
        "1. How does proper cost allocation support accurate profitability analysis?",
        placeholder="Write your thoughts here...",
        key="day19_q1"
    )

    response_2 = st.text_area(
        "2. What challenges might arise in using different cost allocation methods?",
        placeholder="Write your examples here...",
        key="day19_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to deepen your understanding of cost allocation:")
    st.markdown("- [Introduction to Cost Allocation](https://corporatefinanceinstitute.com/resources/knowledge/accounting/cost-allocation/)")
    st.markdown("- [Activity-Based Costing Overview](https://www.investopedia.com/terms/a/abc.asp)")
    st.markdown("- [Best Practices for Cost Allocation](https://www.accountingtools.com/articles/what-are-the-main-cost-allocation-methods.html)")

    st.info("Congratulations on completing Day 19! Tomorrow, we'll explore advanced reporting techniques.")

if __name__ == "__main__":
    day_19_page()
