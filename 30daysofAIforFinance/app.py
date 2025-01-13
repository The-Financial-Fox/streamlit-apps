import streamlit as st
import importlib

def main():
    # Main Page Configuration
    st.set_page_config(
        page_title="30 Days of AI for FP&A and Finance",
        page_icon="📊",
        layout="wide"
    )

    # Header
    st.title("📊 30 Days of AI for FP&A and Finance")
    st.subheader("Learn how to apply AI techniques to Financial Planning and Analysis in just 30 days!")

    # Navigation
    st.sidebar.title("Navigation")
    pages = {"Home": home_page}
    
    # Dynamically load day modules
    for day in range(1, 31):  # Adjust the range if you have fewer/more days
        try:
            day_module = importlib.import_module(f"day_{day}")
            pages[f"Day {day}: {day_module.TITLE}"] = getattr(day_module, f"day_{day}_page")
        except (ModuleNotFoundError, AttributeError):
            pass  # Skip days that haven't been added yet

    page = st.sidebar.radio("Go to:", list(pages.keys()))

    # Render selected page
    pages[page]()


def home_page():
    st.header("Welcome to 30 Days of AI for FP&A and Finance")
    st.write("This program is designed to guide you through the fundamentals of AI and its practical applications in financial planning and analysis.")
    st.write("\n")
    st.markdown("### What's Included:")
    st.markdown("- Daily lessons with hands-on exercises")
    st.markdown("- Practical Streamlit app-building projects")
    st.markdown("- Real-world use cases for FP&A and finance")

    st.markdown("\n")
    st.markdown("### How to Use This App:")
    st.markdown("1. Use the sidebar to navigate to each day's lesson.")
    st.markdown("2. Complete the exercises and build your AI skills.")
    st.markdown("3. Deploy your own Streamlit apps to showcase your learning.")

    st.success("Let’s get started! Choose 'Day 1' from the sidebar to begin.")

if __name__ == "__main__":
    main()
