import streamlit as st

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

    st.header("How It Works")
    st.markdown(
        "- **Daily Lessons**: Each day focuses on a specific topic, building your skills step-by-step."
        "\n- **Interactive Exercises**: Apply what you learn with hands-on tasks."
        "\n- **Real-World Applications**: See how AI can transform FP&A and finance tasks."
    )

    st.header("Connect and Learn More")
    st.write(
        "As you progress through these lessons, feel free to connect with me and explore more resources:"
    )

    st.markdown("**LinkedIn**: [Christian Martinez](https://www.linkedin.com/in/christianmartinezthefinancialfox/)")
    st.markdown("**YouTube**: [Christian Martinez - AI for Finance](https://www.youtube.com/@christianmartinezAIforFinance)")
    st.markdown("**Courses**:")
    st.markdown("- [Advanced ChatGPT for Finance](https://maven.com/nicolas-boucher/advanced-chatgpt-for-finance)")
    st.markdown("- [Python in Excel for Financial Professionals](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-in-excel-for-financial-professionals%3Ftrk%3Dshare_ent_url%26shareId%3DYglnUBKPR3apywIvjWfPdg%253D%253D)")
    st.markdown("- [Advanced Python in Excel & Machine Learning](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fadvanced-python-in-excel-machine-learning%3Ftrk%3Dshare_ent_url%26shareId%3D8BCe%252Bw8mSl6Kcbh1Z4naLw%253D%253D)")
    st.markdown("- [Copilot for Finance Video Course](https://nicolasboucher.gumroad.com/l/Copilot-for-finance-video-course)")

    st.header("Get Started")
    st.write(
        "Select a day from the sidebar to begin your learning journey. Each lesson is designed to be completed in about an hour, making it easy to fit into your schedule."
    )

if __name__ == "__main__":
    main()
