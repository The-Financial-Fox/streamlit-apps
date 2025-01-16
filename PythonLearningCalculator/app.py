import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_recommendation(time_in_excel, tasks_automatable, data_cleanliness, skill_level, complexity, collaboration):
    # Scoring logic: weight each parameter and calculate a score
    score = (time_in_excel * 0.3) + (tasks_automatable * 0.3) + ((5 - data_cleanliness) * 0.1) + \
            (skill_level * 0.1) + (complexity * 0.1) + (collaboration * 0.1)
    
    if score >= 7:
        return "Strongly Recommended", "Learning Python in Excel could save significant time and improve efficiency."
    elif 4 <= score < 7:
        return "Recommended", "Learning Python in Excel could provide moderate benefits."
    else:
        return "Not Urgent", "Python in Excel may not be a priority right now, but keep it in mind for future improvements."

# Streamlit App
st.set_page_config(page_title="FP&A Python in Excel Calculator", page_icon="📊", layout="wide")
st.title("📊 Should FP&A Teams Learn Python in Excel?")
st.markdown("Use this calculator to evaluate whether your team could benefit from learning Python in Excel. Answer a few questions below, and we'll provide a tailored recommendation.")

# Always visible learning section
st.sidebar.header("Start Learning Python in Excel")
st.sidebar.markdown("If you want to start learning Python in Excel, check out the video below:")
st.sidebar.markdown(
    '<iframe width="560" height="315" src="https://www.youtube.com/embed/rN49URY3Q_c?si=G-DoVtxJCGO0UmeN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
    unsafe_allow_html=True
)

# Input fields
with st.container():
    st.header("Your Inputs")
    st.markdown("### Provide information about your team's current processes and challenges:")

    col1, col2 = st.columns(2)
    with col1:
        time_in_excel = st.slider("How many hours per month do you spend in Excel?", 0, 160, 40, help="Estimate the total time spent by your team on Excel-related tasks each month.")
        tasks_automatable = st.slider("How many tasks could be automated with Python?", 0, 50, 10, help="Identify the number of repetitive or manual tasks that could benefit from automation.")
    with col2:
        data_cleanliness = st.radio("How clean is your data?", [
            (1, "Very messy"),
            (2, "Somewhat messy"),
            (3, "Neutral"),
            (4, "Somewhat clean"),
            (5, "Very clean")
        ], help="Rate the quality and consistency of the data you work with.")
        skill_level = st.selectbox("What is your team's Excel skill level?", [1, 2, 3, 4, 5], 
                                  format_func=lambda x: {
                                      1: "Beginner", 2: "Intermediate", 3: "Advanced", 4: "Expert", 5: "Master"
                                  }[x], help="Select the level of proficiency your team has in Excel.")

    complexity = st.slider("How complex are your Excel tasks (e.g., simple reporting to advanced modeling)?", 1, 5, 3, help="Rate the complexity of the tasks your team performs in Excel.")
    collaboration = st.radio("How often does your team collaborate using Excel?", [
        (1, "Rarely"), (2, "Sometimes"), (3, "Often"), (4, "Very Often"), (5, "Always")
    ], help="Indicate how frequently your team collaborates on Excel projects.")

# Calculate recommendation
if st.button("Calculate Recommendation"):
    recommendation, explanation = calculate_recommendation(
        time_in_excel,
        tasks_automatable,
        data_cleanliness[0],  # Extract numeric value from tuple
        skill_level,
        complexity,
        collaboration[0]  # Extract numeric value from tuple
    )
    
    # Display Results
    st.header("Recommendation")
    st.subheader(recommendation)
    st.write(explanation)

    # Visualizations
    st.header("Results Breakdown")
    data = pd.DataFrame({
        "Criteria": ["Time in Excel", "Tasks Automatable", "Data Cleanliness", "Skill Level", "Complexity", "Collaboration"],
        "Score": [time_in_excel, tasks_automatable, 5 - data_cleanliness[0], skill_level, complexity, collaboration[0]]
    })

    col3, col4 = st.columns([2, 1])
    with col3:
        fig = px.bar(data, x="Criteria", y="Score", title="Input Criteria Breakdown", labels={"Score": "Weighted Score"})
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        st.dataframe(data.style.format("{:.2f}"))

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name] - [GitHub Repository](https://github.com/yourusername/fpna-python-excel-calculator)")
