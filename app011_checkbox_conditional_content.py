import streamlit as st

st.title("Checkbox Example")
show_text = st.checkbox("Show text")
if show_text:
    st.write("Here is the hidden text revealed by the checkbox!")
