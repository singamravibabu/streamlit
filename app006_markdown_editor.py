import streamlit as st

st.title("Markdown Editor")
markdown_text = st.text_area("Enter your Markdown text here:")
st.markdown(markdown_text)
