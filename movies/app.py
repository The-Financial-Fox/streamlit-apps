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

# Display dataset summary
st.write("### Dataset Overview")
st.write(df.describe(include='all'))

# Display full dataset for reference
st.write("### Full Dataset")
st.dataframe(df)
