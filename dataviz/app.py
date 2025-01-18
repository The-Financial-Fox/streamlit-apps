import streamlit as st
import pandas as pd
from lida import Summarizer, GoalExplorer, VisGenerator

# Initialize LIDA modules
summarizer = Summarizer()
goal_explorer = GoalExplorer()
vis_generator = VisGenerator()

# Streamlit app
st.title("Excel Data Analyzer and Visualizer with LIDA")

st.sidebar.header("Upload Excel File")
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    # Read the uploaded file
    try:
        data = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(data)

        # Summarize the data
        with st.spinner("Summarizing data..."):
            summary = summarizer.summarize(data)
        st.subheader("Data Summary")
        st.text(summary)

        # Generate visualization goals
        with st.spinner("Exploring visualization goals..."):
            goals = goal_explorer.generate_goals(data)
        st.subheader("Visualization Goals")
        st.write(goals)

        # Select a goal
        st.subheader("Select a Goal for Visualization")
        goal = st.selectbox("Choose a goal:", goals)

        if st.button("Generate Visualization"):
            with st.spinner("Generating visualization..."):
                try:
                    vis_code = vis_generator.generate(data, goal)
                    st.subheader("Visualization Code")
                    st.code(vis_code, language="python")

                    # Execute and render the visualization
                    st.subheader("Visualization Output")
                    exec(vis_code)
                except Exception as e:
                    st.error(f"Error generating visualization: {e}")
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload an Excel file to proceed.")

st.sidebar.markdown("---")
st.sidebar.info("This app uses LIDA to analyze and visualize your data.")
