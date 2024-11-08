import streamlit as st
import random

st.title("Random Quote Generator")

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Do not wait to strike till the iron is hot; but make it hot by striking.",
    "The best way to predict the future is to create it."
]

if st.button("Generate Quote"):
    random_quote = random.choice(quotes)
    st.write(f"**Quote:** {random_quote}")
