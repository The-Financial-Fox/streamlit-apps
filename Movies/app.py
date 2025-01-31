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
    </style>
""", unsafe_allow_html=True)

# **Title**
st.markdown('<h1 class="title">🍿 What Should The 🪺 Nest Watch?</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select from dropdowns or enter your own preferences to get AI-powered movie recommendations!</p>', unsafe_allow_html=True)

# **Dropdowns for User Preferences**
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Fantasy", "Animation", "Documentary"]
movie_types = ["Blockbuster", "Indie", "Cult Classic", "Critically Acclaimed", "Hidden Gem", "Based on a True Story"]
actors = ["Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Scarlett Johansson", "Tom Cruise", "Natalie Portman",
          "Brad Pitt", "Angelina Jolie", "Morgan Freeman", "Emma Stone", "Keanu Reeves", "Joaquin Phoenix"]

st.subheader("🎭 Choose Your Preferences (Dropdowns or Custom Input)")

# **User Choice: Dropdown or Manual Input**
col1, col2 = st.columns(2)

with col1:
    selected_genre = st.selectbox("🎭 Choose a Genre (or type below):", genres)
    selected_type = st.selectbox("🎬 Choose Type of Movie (or type below):", movie_types)
    selected_actor = st.selectbox("🎭 Choose an Actor/Actress (or type below):", actors)

with col2:
    custom_genre = st.text_input("🎭 Or Enter a Genre (if not in dropdown):", "")
    custom_type = st.text_input("🎬 Or Enter a Type of Movie:", "")
    custom_actor = st.text_input("🎭 Or Enter an Actor/Actress:", "")

# **Determine User Selection**
final_genre = custom_genre if custom_genre else selected_genre
final_type = custom_type if custom_type else selected_type
final_actor = custom_actor if custom_actor else selected_actor

# **Generate Movie Recommendation**
if st.button("🎥 Get Movie Recommendation"):
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI movie expert who recommends great films based on user preferences. "
                           "Provide a short, engaging movie recommendation along with a reason why they should watch it."
            },
            {"role": "user", "content": f"Recommend a {final_type} {final_genre} movie starring {final_actor}. "
                                        "Include a short description and why it’s worth watching."}
        ],
        model="llama3-8b-8192",
    )

    movie_recommendation = response.choices[0].message.content

    # **Display Recommendation**
    st.markdown('<div class="movie-container">', unsafe_allow_html=True)
    st.subheader("🎬 AI-Generated Movie Recommendation")
    st.write(movie_recommendation)
    st.markdown('</div>', unsafe_allow_html=True)
