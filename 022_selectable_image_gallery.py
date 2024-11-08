import streamlit as st
from PIL import Image

st.title("Image Gallery")

images = {
    "Mountain": "mountain.jpg",
    "Beach": "beach.jpg",
    "Forest": "forest.jpg"
}

option = st.selectbox("Select an image to view:", list(images.keys()))

if option:
    image = Image.open(images[option])
    st.image(image, caption=option, use_column_width=True)
