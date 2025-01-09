import streamlit as st
import importlib

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
    day_module = importlib.import_module(module_name)
    day_module.run()  # Each day's script must have a `run()` function
except ModuleNotFoundError:
    st.error("🚧 Mini-project for this day is not yet available!")
except Exception as e:
    st.error(f"❌ An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("📘 **Stay Consistent:** Progress is key to success. Let's make every day count!")
