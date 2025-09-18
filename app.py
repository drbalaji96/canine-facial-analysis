import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Canine Facial Analysis",
    page_icon="🐶",
    layout="wide"
)

# --- Title and Introduction ---
st.title('🐶 Canine Facial Assessment Difficulty')
st.write("""
This project analyzes dog faces from the Stanford Dogs dataset to quantify how difficult it is to assess their facial expressions.
A 'difficulty score' was calculated based on facial structure (flatness), hair covering the eyes, and wrinkles.
Below are the top 5 easiest and hardest breeds to assess based on this analysis.
""")

# --- Load Data ---
# These files must also be in your GitHub repository.
try:
    easiest_breeds_df = pd.read_csv('easiest_breeds.csv').set_index('breed')
    hardest_breeds_df = pd.read_csv('hardest_breeds.csv').set_index('breed')
    all_dogs_df = pd.read_csv('dogs_with_scores.csv')
    data_loaded_successfully = True
except FileNotFoundError:
    st.error("Error: Data files not found. Please ensure 'easiest_breeds.csv', 'hardest_breeds.csv', and 'dogs_with_scores.csv' are in the GitHub repository.")
    data_loaded_successfully = False

if data_loaded_successfully:
    # --- Display Charts and Images in two columns ---
    col1, col2 = st.columns(2)

    with col1:
        st.header("❌ Hardest Breeds to Assess")
        st.write("Higher scores indicate features that obscure expressions.")
        st.bar_chart(hardest_breeds_df['difficulty_score'])

        # --- Show Example Images of the Hardest Breed ---
        hardest_breed_name = hardest_breeds_df.index[-1]
        st.subheader(f"Examples: {hardest_breed_name.split('-')[-1].replace('_', ' ')}")
        hardest_images = all_dogs_df[all_dogs_df['breed'] == hardest_breed_name]['image_path'].head(3).tolist()
        st.image(hardest_images, width=200)

    with col2:
        st.header("✅ Easiest Breeds to Assess")
        st.write("Lower scores indicate clearer facial features.")
        st.bar_chart(easiest_breeds_df['difficulty_score'])

        # --- Show Example Images of the Easiest Breed ---
        easiest_breed_name = easiest_breeds_df.index[0]
        st.subheader(f"Examples: {easiest_breed_name.split('-')[-1].replace('_', ' ')}")
        easiest_images = all_dogs_df[all_dogs_df['breed'] == easiest_breed_name]['image_path'].head(3).tolist()
        st.image(easiest_images, width=200)
