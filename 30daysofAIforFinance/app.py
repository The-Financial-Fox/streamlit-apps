import streamlit as st
import importlib

# Main script for 21 Days of AI for FP&A and Finance
st.set_page_config(
    page_title="21 Days of AI for FP&A and Finance",
    page_icon="📊",
    layout="wide"
)

def main():
    st.title("Welcome to 21 Days of AI for FP&A and Finance")
    st.write(
        "Embark on a transformative journey over the next 21 days, where you'll learn the essentials of AI and how to apply it in Financial Planning and Analysis (FP&A). Each day is packed with actionable lessons, interactive exercises, and real-world applications tailored for finance professionals."
    )

    st.sidebar.title("📅 Navigation")
    selected_day = st.sidebar.selectbox(
        "Choose a Day:",
        [f"Day {i}" for i in range(1, 22)]
    )

    try:
        # Dynamically load and run the selected day's script
        day_module = importlib.import_module(f"day_{selected_day.split()[1]}")
        day_module.main()
    except ModuleNotFoundError:
        st.error("Content for this day is not yet available. Please check back later.")

    st.sidebar.markdown("---")
    st.sidebar.title("📢 Connect and Learn More")
    st.sidebar.markdown("[Christian Martinez on LinkedIn](https://www.linkedin.com/in/christianmartinezthefinancialfox/)")
    st.sidebar.markdown("[Christian Martinez on YouTube](https://www.youtube.com/@christianmartinezAIforFinance)")
    st.sidebar.markdown("**Courses:**")
    st.sidebar.markdown("- [Advanced ChatGPT for Finance](https://maven.com/nicolas-boucher/advanced-chatgpt-for-finance)")
    st.sidebar.markdown("- [Python in Excel for Financial Professionals](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-in-excel-for-financial-professionals%3Ftrk%3Dshare_ent_url%26shareId%3DYglnUBKPR3apywIvjWfPdg%253D%253D)")
    st.sidebar.markdown("- [Advanced Python in Excel & Machine Learning](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fadvanced-python-in-excel-machine-learning%3Ftrk%3Dshare_ent_url%26shareId%3D8BCe%252Bw8mSl6Kcbh1Z4naLw%253D%253D)")
    st.sidebar.markdown("- [Copilot for Finance Video Course](https://nicolasboucher.gumroad.com/l/Copilot-for-finance-video-course)")

if __name__ == "__main__":
    main()
