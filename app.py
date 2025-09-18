import streamlit as st
import pandas as pd

st.set_page_config(page_title="Canine Facial Analysis", page_icon="🐶", layout="wide")
st.title('🐶 Canine Facial Assessment Difficulty')
# ... (your intro text) ...

try:
    # Load the single, clean data file from the repository
    df = pd.read_csv('app_data.csv')
    df.dropna(subset=['difficulty_score'], inplace=True)
    
    # Calculate easiest and hardest breeds
    breed_difficulty = df.groupby('breed')['difficulty_score'].mean().sort_values()
    easiest_breeds = breed_difficulty.head(5)
    hardest_breeds = breed_difficulty.tail(5)

    # --- Display Charts and Images ---
    col1, col2 = st.columns(2)
    with col1:
        st.header("❌ Hardest Breeds to Assess")
        st.bar_chart(hardest_breeds)
        hardest_breed_name = hardest_breeds.index[-1]
        st.subheader(f"Examples: {hardest_breed_name.split('-')[-1].replace('_', ' ')}")
        hardest_images = df[df['breed'] == hardest_breed_name]['image_url'].head(3).tolist()
        st.image(hardest_images, width=200)

    with col2:
        st.header("✅ Easiest Breeds to Assess")
        st.bar_chart(easiest_breeds)
        easiest_breed_name = easiest_breeds.index[0]
        st.subheader(f"Examples: {easiest_breed_name.split('-')[-1].replace('_', ' ')}")
        easiest_images = df[df['breed'] == easiest_breed_name]['image_url'].head(3).tolist()
        st.image(easiest_images, width=200)

except FileNotFoundError:
    st.error("Error: 'app_data.csv' not found in the GitHub repository.")
