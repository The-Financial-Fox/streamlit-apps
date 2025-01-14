import streamlit as st

TITLE = "Setting Up Your Environment"

def day_2_page():
    # Header
    st.title(f"🔧 Day 2: {TITLE}")
    st.write("Welcome to Day 2! Today, we'll explore how setting up your environment for AI and Python has never been easier.")

    # Highlight Ease of Setup in 2025
    st.header("No Installations Required!")
    st.write(
        "Using AI and Python in 2025 is easier than ever. You don't need to install anything on your computer if you don't want to! "
        "There are fantastic tools like **Google Colab** and **Python in Excel** that allow you to get started immediately."
    )

    # Recommend Videos
    st.subheader("📺 Recommended Videos")
    st.write("Learn more about these platforms by watching these videos:")
    st.markdown("- [Google Colab for Beginners](https://www.youtube.com/watch?v=d3Ix-UnGlRo&t=1437s)")
    st.markdown("- [Python in Excel Tutorial](https://www.youtube.com/watch?v=rN49URY3Q_c&t=413s)")

    # Introduce Google Colab
    st.header("What is Google Colab?")
    st.write(
        "Google Colab is a free, cloud-based platform that lets you write and execute Python code in a Jupyter Notebook environment. "
        "It requires no setup and runs entirely in your browser."
    )
    st.markdown("### Key Features:")
    st.markdown("- Pre-installed libraries like pandas, NumPy, and TensorFlow.")
    st.markdown("- Access to free GPUs and TPUs for faster computations.")
    st.markdown("- Seamless collaboration and sharing via Google Drive.")

    # Introduce Python in Excel
    st.header("What is Python in Excel?")
    st.write(
        "Python in Excel is a new feature that lets you run Python code directly within Excel. "
        "This allows you to combine the power of Python with the familiarity of Excel for data analysis and financial modeling."
    )
    st.markdown("### Key Features:")
    st.markdown("- Use Python libraries like pandas and matplotlib directly in Excel.")
    st.markdown("- Seamless integration with Excel formulas and functions.")
    st.markdown("- Ideal for financial analysis, visualization, and automation.")

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Choose one of the following tools to explore:")
    st.markdown("1. Open [Google Colab](https://colab.research.google.com/) and create a new notebook.")
    st.markdown("2. Open Excel and enable the Python integration (if available).")
    st.markdown("3. Write a simple Python script to print \"Hello, AI for Finance!\".")

    completed = st.checkbox("I have explored one of the tools.")

    if completed:
        st.success("Great! You're ready to dive into the journey without any installations.")
    else:
        st.warning("Please explore one of the tools to proceed.")

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Here are some resources to help you get started:")
    st.markdown("- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)")
    st.markdown("- [Microsoft Python in Excel Guide](https://support.microsoft.com/en-us/excel)")
    st.markdown("- [Python Basics](https://www.python.org/about/gettingstarted/)")

    st.info("Congratulations on completing Day 2! Come back tomorrow to dive into machine learning basics.")

if __name__ == "__main__":
    day_2_page()
