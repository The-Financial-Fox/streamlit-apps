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

# **Generate Movie Recommendation**
if st.button("🎥 Get Movie Recommendation"):
    client = Groq(api_key=GROQ_API_KEY)
    
    prompt = f"Recommend a {final_type} {final_genre} movie starring {final_actor}."
    if extra_details:
        prompt += f" Also consider these additional preferences: {extra_details}."
    
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI movie expert who recommends great films based on user preferences. "
                           "Provide a short, engaging movie recommendation along with a reason why they should watch it."
            },
            {"role": "user", "content": prompt}
        ],
        model="llama3-8b-8192",
    )

    movie_recommendation = response.choices[0].message.content

    # **Display Recommendation**
    st.markdown('<div class="movie-container">', unsafe_allow_html=True)
    st.subheader("🎬 AI-Generated Movie Recommendation")
    st.write(movie_recommendation)
    st.markdown('</div>', unsafe_allow_html=True)
