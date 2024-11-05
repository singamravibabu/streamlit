import streamlit as st
import time

st.title("Slider and Progress Bar")
slider_value = st.slider("Set the progress", 0, 100)
progress = st.progress(0)

for i in range(slider_value + 1):
    progress.progress(i)
    time.sleep(0.01)
