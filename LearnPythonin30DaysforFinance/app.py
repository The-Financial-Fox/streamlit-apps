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

# Dynamically load and display content for the selected day
try:
    day_number = int(selected_day.split()[1])
    module_name = f"mini_projects.day{day_number}"
    module_path = f"mini_projects/day{day_number}.py"

    # Debugging: Check if the file exists
    if not os.path.exists(module_path):
        raise FileNotFoundError(f"File {module_path} not found!")

    # Debugging: Attempt to import the module
    print(f"Attempting to import: {module_name}")
    day_module = importlib.import_module(module_name)
    print(f"Successfully imported: {module_name}")

    # Call the run() function in the imported module
    if hasattr(day_module, 'run'):
        print(f"Running run() function for {module_name}")
        day_module.run()
    else:
        raise AttributeError(f"The module '{module_name}' does not contain a 'run()' function.")
except ModuleNotFoundError as e:
    st.error("🚧 Mini-project for this day is not yet available!")
    print(f"ModuleNotFoundError: {e}")
except FileNotFoundError as e:
    st.error("🚧 Mini-project file is missing!")
    print(f"FileNotFoundError: {e}")
except AttributeError as e:
    st.error("🚧 The selected day's module does not contain a 'run()' function!")
    print(f"AttributeError: {e}")
except Exception as e:
    st.error(f"❌ An error occurred: {e}")
    print(f"General Exception: {e}")

# Footer
st.markdown("---")
st.markdown("📘 **Stay Consistent:** Progress is key to success. Let's make every day count!")
