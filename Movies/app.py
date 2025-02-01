import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# -------------------------------
# Setup & Environment Variables like API Key
# -------------------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("🚨 API Key is missing! Set it in Streamlit Secrets or a .env file.")
    st.stop()

# -------------------------------
# Page & Session Configurations
# -------------------------------
st.set_page_config(page_title="🎬 Movie Magic", page_icon="🍿", layout="wide")

# Initialize session state for recommendation history
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Custom CSS for a Modern Look
# -------------------------------
st.markdown("""
    <style>
        /* Global styling */
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #ffcc00;
            margin-top: 20px;
        }
        .subtitle {
            text-align: center;
            font-size: 22px;
            color: #cccccc;
            margin-bottom: 40px;
        }
        .stButton > button {
            width: 100%;
            background-color: #ffcc00;
            color: #000;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 5px;
        }
        .movie-container {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        }
        /* Styling for input elements */
        input, select, textarea {
            background-color: #2a2a2a !important;
            color: #ffffff !important;
            border: 1px solid #444444 !important;
        }
        /* Sidebar styling */
        .css-1d391kg {  /* streamlit default sidebar class might change in future versions */
            background-color: #1e1e1e;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Navigation
# -------------------------------
st.sidebar.title("Movie Magic Navigation")
app_mode = st.sidebar.radio("Go to", ["Home", "Recommendation History", "About"])

# -------------------------------
# Helper Function for API Call
# -------------------------------
def get_movie_recommendation(final_genre, final_type, final_actor, extra_details):
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
    recommendation = response.choices[0].message.content
    return recommendation

# -------------------------------
# Main App Pages
# -------------------------------
if app_mode == "Home":
    # Header Banner Image (you can replace the URL with your own image)
    st.image("https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
             use_column_width=True)
    st.markdown('<h1 class="title">🍿 Movie Magic</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Your ultimate destination for AI-powered movie recommendations!</p>', unsafe_allow_html=True)

    st.markdown("### 🎭 Choose Your Preferences")
    
    # Options for Dropdowns
    genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Fantasy", "Animation", "Documentary", "Other"]
    movie_types = ["Blockbuster", "Indie", "Cult Classic", "Critically Acclaimed", "Hidden Gem", "Based on a True Story", "Other"]
    actors = ["Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Scarlett Johansson", "Tom Cruise", "Natalie Portman",
              "Brad Pitt", "Angelina Jolie", "Morgan Freeman", "Emma Stone", "Keanu Reeves", "Joaquin Phoenix", "Other"]
    
    # Two-column layout for dropdowns and custom input
    col1, col2 = st.columns(2)
    with col1:
        selected_genre = st.selectbox("🎭 Choose a Genre:", genres, index=0)
        selected_type = st.selectbox("🎬 Choose Movie Type:", movie_types, index=0)
        selected_actor = st.selectbox("🌟 Choose an Actor/Actress:", actors, index=0)
    with col2:
        custom_genre = st.text_input("If 'Other', enter Genre:") if selected_genre == "Other" else ""
        custom_type = st.text_input("If 'Other', enter Movie Type:") if selected_type == "Other" else ""
        custom_actor = st.text_input("If 'Other', enter Actor/Actress:") if selected_actor == "Other" else ""
    
    # Determine final values
    final_genre = custom_genre if selected_genre == "Other" and custom_genre else selected_genre
    final_type = custom_type if selected_type == "Other" and custom_type else selected_type
    final_actor = custom_actor if selected_actor == "Other" and custom_actor else selected_actor

    st.markdown("### 📝 Any Extra Details?")
    extra_details = st.text_area("💡 Add any additional preferences (e.g., 'uplifting story', 'set in space', 'great soundtrack')", "")

    if st.button("🎥 Get Movie Recommendation"):
        with st.spinner("Finding the perfect movie for you..."):
            recommendation = get_movie_recommendation(final_genre, final_type, final_actor, extra_details)
            # Save recommendation to session history
            st.session_state.history.append({
                "genre": final_genre,
                "type": final_type,
                "actor": final_actor,
                "extra": extra_details,
                "recommendation": recommendation
            })
            st.markdown('<div class="movie-container">', unsafe_allow_html=True)
            st.subheader("🎬 Your AI-Generated Recommendation")
            st.write(recommendation)
            st.markdown('</div>', unsafe_allow_html=True)

elif app_mode == "Recommendation History":
    st.markdown('<h1 class="title">📜 Recommendation History</h1>', unsafe_allow_html=True)
    if st.session_state.history:
        for idx, rec in enumerate(reversed(st.session_state.history), start=1):
            with st.expander(f"Recommendation #{idx} - {rec['genre']} | {rec['type']} | {rec['actor']}"):
                st.write(f"**Genre:** {rec['genre']}")
                st.write(f"**Movie Type:** {rec['type']}")
                st.write(f"**Actor/Actress:** {rec['actor']}")
                if rec["extra"]:
                    st.write(f"**Extra Details:** {rec['extra']}")
                st.markdown("---")
                st.write(rec["recommendation"])
    else:
        st.info("No recommendations yet. Head over to the Home page to get started!")
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.success("History cleared!")

elif app_mode == "About":
    st.markdown('<h1 class="title">ℹ️ About Movie Magic</h1>', unsafe_allow_html=True)
    st.write("""
    **Movie Magic** is a fun, AI-powered movie recommendation app built with Streamlit. 
    Whether you're in the mood for a blockbuster hit or a hidden gem, our app tailors suggestions to your unique tastes.

    **Features:**
    - **Personalized Recommendations:** Based on your favorite genres, movie types, and actors.
    - **History:** Keep track of all your past recommendations.
    - **Modern UI:** Enjoy a sleek, immersive design that makes movie browsing a delight.

    **Developed with ❤️ by [Your Name].**
    """)
    st.image("https://images.unsplash.com/photo-1558980394-0e156d6eaff0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
             use_column_width=True)
    st.markdown("Feel free to reach out with any feedback or suggestions!")
