import streamlit as st
import importlib
import os

# Page Configuration
st.set_page_config(
    page_title="30 Days of Python for FP&A",
    page_icon="📊",
    layout="wide"
)

# Header Section
st.title("📊 30 Days to Learn Python for FP&A")
st.markdown("""
Welcome to **30 Days of Python for FP&A**, a journey to master Python concepts and tools for Financial Planning and Analysis. 
Each day covers a new concept with mini-projects to apply your knowledge.
""")

# Sidebar Navigation
st.sidebar.title("📅 Day Selector")
selected_day = st.sidebar.selectbox("Choose a day to explore:", [f"Day {i}" for i in range(1, 31)])

# Main Content Area
st.write(f"## {selected_day}: Mini-Project")

# Debug: Check if the module and file exist
try:
    day_number = int(selected_day.split()[1])
    module_name = f"mini_projects.day{day_number}"
    module_path = f"mini_projects/day{day_number}.py"

    # Check if the file exists
    if not os.path.exists(module_path):
        raise FileNotFoundError(f"File '{module_path}' does not exist!")

    # Attempt to import the module
    day_module = importlib.import_module(module_name)

    # Run the `run()` function if it exists
    if hasattr(day_module, 'run'):
        day_module.run()
    else:
        raise AttributeError(f"The module '{module_name}' does not contain a 'run()' function.")
except FileNotFoundError as e:
    st.error(f"🚧 Mini-project file for {selected_day} is missing!")
    print(e)
except ModuleNotFoundError as e:
    st.error(f"🚧 Mini-project module for {selected_day} is not found!")
    print(e)
except AttributeError as e:
    st.error(f"🚧 The module for {selected_day} does not contain a 'run()' function!")
    print(e)
except Exception as e:
    st.error(f"❌ An unexpected error occurred: {e}")
    print(e)

# Footer
st.markdown("---")
st.markdown("📘 **Stay Consistent:** Progress is key to success. Let's make every day count!")
