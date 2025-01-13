import streamlit as st

def day_1_page():
    st.set_page_config(
        page_title="Day 1: Overview of AI in FP&A",
        page_icon="\ud83d\udcca",
        layout="wide"
    )

    st.title("\ud83d\udcca Day 1: Overview of AI in FP&A")
    st.write("Welcome to Day 1! Today we will explore the basics of AI and its applications in Financial Planning and Analysis (FP&A).")

    st.header("Key Topics")
    st.markdown("- **What is Artificial Intelligence (AI)?**")
    st.markdown("- **Use cases for AI in FP&A:** Budgeting, Forecasting, Anomaly Detection, and Scenario Planning.")
    st.markdown("- **Benefits and challenges of adopting AI in Finance.**")

    st.header("Today's Exercise")
    st.write("Reflect on these questions and share your insights:")

    st.text_area(
        "1. What are some challenges in FP&A that you think AI can solve?",
        placeholder="Write your thoughts here...",
        key="day1_q1"
    )

    st.text_area(
        "2. Can you think of specific examples in your work or studies where AI could be applied to improve outcomes?",
        placeholder="Write your examples here...",
        key="day1_q2"
    )

    st.info("Congratulations on completing Day 1! Come back tomorrow to dive into setting up your environment.")

if __name__ == "__main__":
    day_1_page()
