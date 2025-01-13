import streamlit as st

TITLE = "Setting Up Your Environment"

def day_2_page():
    # Header
    st.title(f"🔧 Day 2: {TITLE}")
    st.write("Welcome to Day 2! Today, we'll set up the tools and environment needed to embark on your 30-day AI journey.")

    # Key Topics Section
    st.header("Key Topics")
    st.markdown("- **Installing Python and Required Libraries**")
    st.markdown("- **Setting Up Jupyter and Streamlit**")
    st.markdown("- **Introduction to pandas and NumPy**")

    # Step-by-Step Setup Guide
    st.header("Step-by-Step Setup Guide")
    st.markdown("1. **Install Python**: Download and install the latest version of Python from [python.org](https://www.python.org/downloads/).")
    st.markdown("2. **Set Up a Virtual Environment**: Run the following commands to create and activate a virtual environment:")
    st.code("""\npython -m venv ai_env\nsource ai_env/bin/activate  # On Windows: ai_env\\Scripts\\activate\n""", language="bash")
    st.markdown("3. **Install Required Libraries**: Use pip to install the necessary libraries:")
    st.code("pip install streamlit pandas numpy matplotlib scikit-learn")
    st.markdown("4. **Install Jupyter Notebook**: Run the command:")
    st.code("pip install notebook")
    st.markdown("5. **Test Streamlit Installation**: Verify that Streamlit is installed correctly by running:")
    st.code("streamlit hello")

    # Interactive Exercise
    st.header("Today's Exercise")
    st.markdown("Complete the following tasks:")
    st.markdown("1. Install Python and set up a virtual environment.")
    st.markdown("2. Install the required libraries and Jupyter Notebook.")
    st.markdown("3. Run the Streamlit 'hello' app to ensure everything is working.")

    completed = st.checkbox("I have completed today's setup tasks.")

    if completed:
        st.success("Great! You're all set to continue the journey.")
    else:
        st.warning("Please complete the setup tasks to proceed.")

    # Additional Learning Resources
    st.header("Additional Resources")
    st.write("Here are some resources to help you with the setup process:")
    st.markdown("- [Official Python Downloads](https://www.python.org/downloads/)")
    st.markdown("- [Getting Started with Streamlit](https://docs.streamlit.io/library/get-started)")
    st.markdown("- [Jupyter Notebook Documentation](https://jupyter.org/documentation)")

    st.info("Congratulations on completing Day 2! Come back tomorrow to dive into machine learning basics.")

if __name__ == "__main__":
    day_2_page()
