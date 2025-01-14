import streamlit as st

TITLE = "Overview of AI in FP&A"

def day_1_page():
    # Header
    st.title(f"📊 Day 1: {TITLE}")
    st.write("Welcome to Day 1! Today we will explore the basics of AI and its applications in Financial Planning and Analysis (FP&A).")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **What is Artificial Intelligence (AI)?**")
    st.markdown("- **Use cases for AI in FP&A:** Budgeting, Forecasting, Anomaly Detection, and Scenario Planning.")
    st.markdown("- **Benefits and challenges of adopting AI in Finance.**")

     # Recommend Videos with Embedding
    st.subheader("📺 Recommended Videos")
    st.write("Learn more about these platforms by watching these videos:")

    st.markdown("**Using AI for Finance and FP&A**")
    st.components.v1.iframe(
        src="https://www.youtube.com/watch?v=4IzcGV6fCEA&t=2s",
        width=560,
        height=315
    )

    # Interactive Exercise Section
    st.header("Today's Exercise")
    st.markdown("Reflect on these questions and share your insights:")

    response_1 = st.text_area(
        "1. What are some challenges in FP&A that you think AI can solve?",
        placeholder="Write your thoughts here...",
        key="day1_q1"
    )

    response_2 = st.text_area(
        "2. Can you think of specific examples in your work or studies where AI could be applied to improve outcomes?",
        placeholder="Write your examples here...",
        key="day1_q2"
    )

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Explore these resources to learn more about AI in FP&A:")
    st.markdown("- [Introduction to AI](https://en.wikipedia.org/wiki/Artificial_intelligence)")
    st.markdown("- [Applications of AI in Finance](https://www.forbes.com/sites/forbestechcouncil/2021/05/14/ai-in-finance/)")
    st.markdown("- [FP&A and AI Use Cases](https://www.gartner.com/en/finance/fp-a)")

    # Save Progress
    if st.button("Save Progress"):
        st.success("Your responses have been saved. Great work on Day 1!")

    st.info("Congratulations on completing Day 1! Come back tomorrow to dive into setting up your environment.")

if __name__ == "__main__":
    day_1_page()
