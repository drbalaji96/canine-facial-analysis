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
A 'difficulty score' was calculated based on facial structure, hair covering the eyes, and wrinkles.
Below are the top 5 easiest and hardest breeds to assess based on this analysis.
""")

# --- Load Data ---
# We only need the two small analysis files now.
try:
    easiest_breeds_df = pd.read_csv('easiest_breeds.csv').set_index('breed')
    hardest_breeds_df = pd.read_csv('hardest_breeds.csv').set_index('breed')
    data_loaded_successfully = True
except FileNotFoundError:
    st.error("Error: Analysis files not found. Please ensure 'easiest_breeds.csv' and 'hardest_breeds.csv' are in the GitHub repository.")
    data_loaded_successfully = False

if data_loaded_successfully:
    # --- Define local image paths ---
    hardest_images = ['example_images/hardest_1.jpg', 'example_images/hardest_2.jpg', 'example_images/hardest_3.jpg']
    easiest_images = ['example_images/easiest_1.jpg', 'example_images/easiest_2.jpg', 'example_images/easiest_3.jpg']

    # --- Display Charts and Images in two columns ---
    col1, col2 = st.columns(2)

    with col1:
        st.header("❌ Hardest Breeds to Assess")
        st.write("Higher scores indicate features that obscure expressions.")
        st.bar_chart(hardest_breeds_df['difficulty_score'])

        hardest_breed_name = hardest_breeds_df.index[-1]
        st.subheader(f"Examples: {hardest_breed_name.split('-')[-1].replace('_', ' ')}")
        st.image(hardest_images, width=200)

    with col2:
        st.header("✅ Easiest Breeds to Assess")
        st.write("Lower scores indicate clearer facial features.")
        st.bar_chart(easiest_breeds_df['difficulty_score'])
        
        easiest_breed_name = easiest_breeds_df.index[0]
        st.subheader(f"Examples: {easiest_breed_name.split('-')[-1].replace('_', ' ')}")
        st.image(easiest_images, width=200)
