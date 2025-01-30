import streamlit as st
import pandas as pd

# Load data
def load_data():
    file_url = "https://raw.githubusercontent.com/The-Financial-Fox/streamlit-apps/refs/heads/main/movies/Top_1000_IMDb_movies_New_version.csv"
    df = pd.read_csv(file_url)
    st.write("### First few rows of dataset:")
    st.write(df.head())  # Debugging: Show the first few rows
    st.write("### Dataset Columns:", df.columns.tolist())  # Debugging: Show column names
    return df

df = load_data()

# Streamlit app
st.title("🎬 Movie Recommendation App")
st.write("Find the perfect movie to watch!")

# Ensure required columns exist
required_columns = ['Genre', 'Year', 'IMDb Rating', 'Title', 'Runtime', 'Description']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    st.error(f"Missing columns in dataset: {missing_columns}")
else:
    # Filters
    st.sidebar.header("Filter movies")
    selected_genre = st.sidebar.multiselect("Select Genre", df['Genre'].dropna().unique())
    selected_year = st.sidebar.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()), (2000, 2024))
    selected_rating = st.sidebar.slider("Select IMDb Rating", float(df['IMDb Rating'].min()), float(df['IMDb Rating'].max()), (7.0, 10.0))

    # Filter dataset
    filtered_df = df.copy()
    if selected_genre:
        filtered_df = filtered_df[df['Genre'].apply(lambda x: any(genre in str(x) for genre in selected_genre))]
    filtered_df = filtered_df[(filtered_df['Year'] >= selected_year[0]) & (filtered_df['Year'] <= selected_year[1])]
    filtered_df = filtered_df[(filtered_df['IMDb Rating'] >= selected_rating[0]) & (filtered_df['IMDb Rating'] <= selected_rating[1])]

    # Display movies
    st.subheader("Recommended Movies")
    if not filtered_df.empty:
        for index, row in filtered_df.iterrows():
            st.markdown(f"### {row['Title']} ({row['Year']})")
            st.text(f"⭐ {row['IMDb Rating']} | 🎭 {row['Genre']} | ⏳ {row['Runtime']} mins")
            st.write(row['Description'])
            st.markdown("---")
    else:
        st.write("No movies found with selected filters.")

# Deployment instructions
st.sidebar.markdown("### Deployment Instructions")
st.sidebar.text("1. Push this code to GitHub.")
st.sidebar.text("2. Upload 'requirements.txt'.")
st.sidebar.text("3. Deploy on Streamlit Community Cloud.")
