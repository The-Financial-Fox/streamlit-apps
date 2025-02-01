import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load API key securely
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("🚨 API Key is missing! Set it in Streamlit Secrets or a .env file.")
    st.stop()

# **🎬 Streamlit App UI**
st.set_page_config(page_title="What Should The 🪺 Nest Watch?", page_icon="🍿", layout="wide")

# **Custom Styling**
st.markdown("""
    <style>
        .title { text-align: center; font-size: 36px; font-weight: bold; color: #ffcc00; }
        .subtitle { text-align: center; font-size: 20px; color: #dddddd; }
        .stButton>button { width: 100%; background-color: #ffcc00; color: black; font-size: 16px; font-weight: bold; }
        .stSelectbox, .stTextInput { text-align: center; }
        .movie-container { text-align: center; margin-top: 20px; }
        .recommendation { margin-bottom: 20px; padding: 10px; background-color: #333333; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# **Title**
st.markdown('<h1 class="title">🍿 What Should The 🪺 Nest Watch?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select from dropdowns or enter your own preferences to get AI-powered movie recommendations!</p>', unsafe_allow_html=True)

# **Dropdowns for User Preferences**
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Fantasy", "Animation", "Documentary", "Other"]
movie_types = ["Blockbuster", "Indie", "Cult Classic", "Critically Acclaimed", "Hidden Gem", "Based on a True Story", "Other"]
actors = ["Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Scarlett Johansson", "Tom Cruise", "Natalie Portman",
          "Brad Pitt", "Angelina Jolie", "Morgan Freeman", "Emma Stone", "Keanu Reeves", "Joaquin Phoenix", "Other"]

st.subheader("🎭 Choose Your Preferences (Dropdowns or Custom Input)")

# **User Choice: Dropdown or Manual Input**
col1, col2 = st.columns(2)

with col1:
    selected_genre = st.selectbox("🎭 Choose a Genre:", genres)
    selected_type = st.selectbox("🎬 Choose Type of Movie:", movie_types)
    selected_actor = st.selectbox("🎭 Choose an Actor/Actress:", actors)

with col2:
    custom_genre = st.text_input("🎭 If 'Other', Enter Genre:", "") if selected_genre == "Other" else ""
    custom_type = st.text_input("🎬 If 'Other', Enter Type of Movie:", "") if selected_type == "Other" else ""
    custom_actor = st.text_input("🎭 If 'Other', Enter Actor/Actress:", "") if selected_actor == "Other" else ""

# **Determine Final User Selection**
final_genre = custom_genre if selected_genre == "Other" else selected_genre
final_type = custom_type if selected_type == "Other" else selected_type
final_actor = custom_actor if selected_actor == "Other" else selected_actor

# **Additional Details for Personalized Recommendation**
st.subheader("📝 Any Extra Details? (Optional)")
extra_details = st.text_area("💡 Add anything else about the kind of movie you’d like to watch! (e.g., 'I want something uplifting', 'Set in space', 'Great soundtrack')", "")

# **Generate Movie Recommendations**
if st.button("🎥 Get Movie Recommendations"):
    client = Groq(api_key=GROQ_API_KEY)
    
    # Build the prompt with streaming details
    prompt = (
        f"Recommend three {final_type} {final_genre} movies starring {final_actor}. "
        "For each recommendation, provide the movie title, a brief explanation of why it is worth watching, "
        "and mention one streaming platform (choose from Netflix, Amazon Prime, Disney Plus, or Apple TV) where the movie is available."
    )
    if extra_details:
        prompt += f" Also consider these additional preferences: {extra_details}."
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI movie expert who provides engaging movie recommendations. "
                    "Respond with three separate movie recommendations. For each, include the movie title, "
                    "a brief reason why the viewer should watch it, and the name of one streaming platform (Netflix, Amazon Prime, Disney Plus, or Apple TV) where the movie is available."
                )
            },
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192",
    )

    movie_recommendations = response.choices[0].message.content

    # **Display Recommendations**
    st.markdown('<div class="movie-container">', unsafe_allow_html=True)
    st.subheader("🎬 AI-Generated Movie Recommendations")
    st.markdown(movie_recommendations)
    st.markdown('</div>', unsafe_allow_html=True)
