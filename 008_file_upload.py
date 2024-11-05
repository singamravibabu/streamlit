import streamlit as st

st.title("File Upload Example")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.write("File content:")
    st.text(content)
