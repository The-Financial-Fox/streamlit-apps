import streamlit as st
import importlib

def main():
    # Main Page Configuration
    st.set_page_config(
        page_title="21 Days of AI for FP&A and Finance",
        page_icon="📊",
        layout="wide"
    )

    # Header
    st.title("📊 21 Days of AI for FP&A and Finance")
    st.subheader("Learn how to apply AI techniques to Financial Planning and Analysis in just 30 days!")

    # Navigation
    st.sidebar.title("Navigation")
    pages = {"Home": home_page}

    # Dynamically load day modules
    for day in range(1, 31):  # Adjust range if necessary
        try:
            day_module = importlib.import_module(f"day_{day}")
            pages[f"Day {day}: {day_module.TITLE}"] = getattr(day_module, f"day_{day}_page")
        except (ModuleNotFoundError, AttributeError):
            pass  # Skip days that haven't been added yet

    page = st.sidebar.radio("Go to:", list(pages.keys()))

    # Render selected page
    pages[page]()


def home_page():
    st.header("Welcome to 21 Days of AI for FP&A and Finance")
    st.write("This program is designed to guide you through the fundamentals of AI and its practical applications in financial planning and analysis.")
    st.markdown("### What's Included:")
    st.markdown("- Daily lessons with hands-on exercises")
    st.markdown("- Practical Streamlit app-building projects")
    st.markdown("- Real-world use cases for FP&A and finance")

    # Embed YouTube video
    st.subheader("📺 Watch the Introduction Video")
    st.components.v1.iframe(
        src="https://www.youtube.com/embed/liN9IgGES7k?si=Ckm44bwOFENuv8lj",
        width=560,
        height=315
    )

    st.markdown("📢 Connect and Learn More")
    st.markdown("[Christian Martinez on LinkedIn](https://www.linkedin.com/in/christianmartinezthefinancialfox/)")
    st.markdown("[Christian Martinez on YouTube](https://www.youtube.com/@christianmartinezAIforFinance)")
    # Add Image
    st.image(
        "https://raw.githubusercontent.com/The-Financial-Fox/streamlit-apps/refs/heads/main/30daysofAIforFinance/How%20to%20Learn%20AI%20for%20Finance%20Fast.png",
        caption="How to Learn AI for Finance Fast by Christian Martinez",
        use_column_width=True
    )

    st.markdown("**Courses:**")
    st.markdown("- [Advanced ChatGPT for Finance](https://maven.com/nicolas-boucher/advanced-chatgpt-for-finance)")
    st.markdown("- [Python in Excel for Financial Professionals](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fpython-in-excel-for-financial-professionals%3Ftrk%3Dshare_ent_url%26shareId%3DYglnUBKPR3apywIvjWfPdg%253D%253D)")
    st.markdown("- [Advanced Python in Excel & Machine Learning](https://www.linkedin.com/learning-login/share?forceAccount=false&redirect=https%3A%2F%2Fwww.linkedin.com%2Flearning%2Fadvanced-python-in-excel-machine-learning%3Ftrk%3Dshare_ent_url%26shareId%3D8BCe%252Bw8mSl6Kcbh1Z4naLw%253D%253D)")
    st.markdown("- [Copilot for Finance Video Course](https://nicolasboucher.gumroad.com/l/Copilot-for-finance-video-course)")

    st.success("Let’s get started! Choose 'Day 1' from the sidebar to begin.")


if __name__ == "__main__":
    main()
