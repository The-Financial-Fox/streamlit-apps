import streamlit as st

TITLE = "Recap and Next Steps"

def day_21_page():
    # Header
    st.title(f"🎉 Day 21: {TITLE}")
    st.write("Congratulations on completing 21 days of learning AI for FP&A and Finance!")

    # Recap Section
    st.header("Recap of Our Journey")
    st.markdown("Over the past 21 days, we have explored:")
    st.markdown("- **Day 1 to 5**: Introduction to AI, setting up your environment, and learning the basics of machine learning.")
    st.markdown("- **Day 6 to 10**: Visualizations, time-series analysis, clustering, and predictive modeling.")
    st.markdown("- **Day 11 to 15**: Advanced classification, regression, optimization techniques, dashboards, and KPI tracking.")
    st.markdown("- **Day 16 to 20**: Scenario planning, sensitivity analysis, advanced forecasting, cost allocation, and data storytelling.")
    st.markdown("Each day brought new tools and techniques to transform how we approach FP&A and finance with AI.")

    # Thank You Section
    st.header("A Heartfelt Thank You")
    st.markdown("Thank you for being part of this incredible journey! Your commitment to learning and advancing in finance and AI is inspiring.")

    # Connect with Me
    st.header("Stay Connected")
    st.write("I would love to continue supporting your learning journey. Connect with me and explore more resources:")

    st.markdown("**LinkedIn**: [Christian Martinez](https://www.linkedin.com/in/christianmartinezthefinancialfox/)")
    st.markdown("**YouTube**: [Christian Martinez - AI for Finance](https://www.youtube.com/@christianmartinezAIforFinance)")
    st.markdown("**Courses**:")
    st.markdown("- [Advanced ChatGPT for Finance](https://maven.com/nicolas-boucher/advanced-chatgpt-for-finance)")
    st.markdown("- [Python in Excel for Financial Professionals](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-in-excel-for-financial-professionals%3Ftrk%3Dshare_ent_url%26shareId%3DYglnUBKPR3apywIvjWfPdg%253D%253D)")
    st.markdown("- [Advanced Python in Excel & Machine Learning](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fadvanced-python-in-excel-machine-learning%3Ftrk%3Dshare_ent_url%26shareId%3D8BCe%252Bw8mSl6Kcbh1Z4naLw%253D%253D)")
    st.markdown("- [Copilot for Finance Video Course](https://nicolasboucher.gumroad.com/l/Copilot-for-finance-video-course)")

    # Closing Message
    st.header("Looking Ahead")
    st.markdown("This is just the beginning! The skills and techniques you've learned over these 21 days are a foundation for greater success in leveraging AI for FP&A and Finance.")
    st.markdown("Keep exploring, practicing, and innovating. The future of finance is AI-driven, and you are now equipped to be at the forefront of this transformation.")

    st.balloons()

if __name__ == "__main__":
    day_21_page()
