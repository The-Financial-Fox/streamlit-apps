import streamlit as st

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
    st.info("Navigate to each day's lesson by adding it to the folder structure.")

    # Welcome Message
    st.header("Welcome to 30 Days of AI for FP&A and Finance")
    st.write("This program is designed to guide you through the fundamentals of AI and its practical applications in financial planning and analysis.")
    st.write("\n")
    st.markdown("### What's Included:")
    st.markdown("- Daily lessons with hands-on exercises")
    st.markdown("- Practical Streamlit app-building projects")
    st.markdown("- Real-world use cases for FP&A and finance")

    st.markdown("\n")
    st.markdown("### How to Use This App:")
    st.markdown("1. Use the sidebar to navigate to each day's lesson as you add them.")
    st.markdown("2. Complete the exercises and build your AI skills.")
    st.markdown("3. Deploy your own Streamlit apps to showcase your learning.")

    st.success("Let’s get started! Add the first day's content to the folder and navigate to it using the sidebar.")

if __name__ == "__main__":
    main()
