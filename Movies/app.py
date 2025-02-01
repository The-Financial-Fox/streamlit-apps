import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("🚨 API Key is missing! Set it in Streamlit Secrets or a .env file.")
    st.stop()

# -------------------------------
# Set Page Configuration
# -------------------------------
st.set_page_config(page_title="🍿 Movie Magic", page_icon="🍿", layout="centered")

# -------------------------------
# Custom CSS for a Fancy Look
# -------------------------------
st.markdown("""
    <style>
        /* Gradient background for the whole app */
        body {
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            margin-top: 20px;
            color: #ffffff;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            margin-bottom: 40px;
            color: #f0f0f0;
        }
        .stButton > button {
            background-color: #ffcc00;
            color: #000;
            font-size: 20px;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
        }
        .input-box {
            background-color: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .result-box {
            background-color: rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        /* Style for text inputs, select boxes, and text areas */
        input, select, textarea {
            background-color: rgba(255, 255, 255, 0.2) !important;
            color: #ffffff !important;
            border: 1px solid #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# App Header
# -------------------------------
st.markdown('<h1 class="title">🍿 Movie Magic</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your AI-powered movie recommendation assistant</p>', unsafe_allow_html=True)

# -------------------------------
# User Input Section
# -------------------------------
with st.container():
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    
    # Genre selection
    genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Fantasy", "Animation", "Documentary", "Other"]
    selected_genre = st.selectbox("Select Genre", genres)
    custom_genre = ""
    if selected_genre == "Other":
        custom_genre = st.text_input("Enter your preferred genre:")
    
    # Movie type selection
    movie_types = ["Blockbuster", "Indie", "Cult Classic", "Critically Acclaimed", "Hidden Gem", "Based on a True Story", "Other"]
    selected_type = st.selectbox("Select Movie Type", movie_types)
    custom_type = ""
    if selected_type == "Other":
        custom_type = st.text_input("Enter your preferred movie type:")
    
    # Actor selection
    actors = ["Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Scarlett Johansson", "Tom Cruise", "Natalie Portman",
              "Brad Pitt", "Angelina Jolie", "Morgan Freeman", "Emma Stone", "Keanu Reeves", "Joaquin Phoenix", "Other"]
    selected_actor = st.selectbox("Select Actor/Actress", actors)
    custom_actor = ""
    if selected_actor == "Other":
        custom_actor = st.text_input("Enter your preferred actor/actress:")
    
    # Extra details (optional)
    extra_details = st.text_area("Any extra details? (Optional)", placeholder="e.g., uplifting story, set in space, great soundtrack")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Determine the final values
    final_genre = custom_genre if selected_genre == "Other" and custom_genre else selected_genre
    final_type = custom_type if selected_type == "Other" and custom_type else selected_type
    final_actor = custom_actor if selected_actor == "Other" and custom_actor else selected_actor

# -------------------------------
# Generate and Display Recommendation
# -------------------------------
if st.button("🎥 Get Recommendation"):
    with st.spinner("Finding your perfect movie..."):
        client = Groq(api_key=GROQ_API_KEY)
        prompt = f"Recommend a {final_type} {final_genre} movie starring {final_actor}."
        if extra_details:
            prompt += f" Also consider these preferences: {extra_details}."
        
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an AI movie expert who provides short, engaging movie recommendations with reasons."},
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192",
        )
        recommendation = response.choices[0].message.content
        
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🎬 Your Recommendation")
        st.write(recommendation)
        st.markdown('</div>', unsafe_allow_html=True)
