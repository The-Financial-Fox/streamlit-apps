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
st.title("Should FP&A Teams Learn Python in Excel?")
st.markdown("Use this calculator to evaluate whether your team could benefit from learning Python in Excel.")

# Input fields
with st.container():
    st.header("Your Inputs")
    time_in_excel = st.slider("How many hours per month do you spend in Excel?", 0, 160, 40)
    tasks_automatable = st.slider("How many tasks could be automated with Python?", 0, 50, 10)
    data_cleanliness = st.radio("How clean is your data?", [
        (1, "Very messy"),
        (2, "Somewhat messy"),
        (3, "Neutral"),
        (4, "Somewhat clean"),
        (5, "Very clean")
    ])
    skill_level = st.selectbox("What is your team's Excel skill level?", [1, 2, 3, 4, 5], format_func=lambda x: {
        1: "Beginner", 2: "Intermediate", 3: "Advanced", 4: "Expert", 5: "Master"
    }[x])
    complexity = st.slider("How complex are your Excel tasks (e.g., simple reporting to advanced modeling)?", 1, 5, 3)
    collaboration = st.radio("How often does your team collaborate using Excel?", [
        (1, "Rarely"), (2, "Sometimes"), (3, "Often"), (4, "Very Often"), (5, "Always")
    ])

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
    st.dataframe(data)
    fig = px.bar(data, x="Criteria", y="Score", title="Input Criteria Breakdown")
    st.plotly_chart(fig)

# Always visible learning section
st.markdown("---")
st.markdown("### Start Learning Python in Excel")
st.markdown("If you want to start learning Python in Excel, check out the video below:")
st.markdown(
    '<iframe width="560" height="315" src="https://www.youtube.com/embed/rN49URY3Q_c?si=G-DoVtxJCGO0UmeN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown("Developed by [Christian Martinez] - [GitHub Repository](https://github.com/The-Financial-Fox/pythonforfinance2025)")

