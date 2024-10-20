import streamlit as st
from PIL import Image
import os

# Store animal images locally (make sure to replace the paths with actual paths to your images)
animal_images = {
    "Cat": "image/cat_image.png",  # replace with your local path
    "Dog": "image/dog_image.png",  # replace with your local path
    "Elephant": "image/elephant_image.png",  # replace with your local path
}

# Title for the app
st.title("Animal Selection and File Upload")

# Checkbox for animal selection
st.subheader("Select an animal:")
selected_animal = st.radio("Choose an animal", ["Cat", "Dog", "Elephant"])

# Display corresponding animal image
if selected_animal:
    st.image(
        Image.open(animal_images[selected_animal]),
        caption=f"Here is a {selected_animal}!",
        use_column_width=True,
    )

# File uploader
st.subheader("Upload a file:")
uploaded_file = st.file_uploader("Choose a file")

# Display file details if a file is uploaded
if uploaded_file is not None:
    file_details = {
        "Filename": uploaded_file.name,
        "File Size": f"{uploaded_file.size / 1000} KB",
        "File Type": uploaded_file.type,
    }
    st.write("Uploaded File Details:")
    st.json(file_details)
