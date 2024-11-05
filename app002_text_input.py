import streamlit as st

st.title("Simple Text Input App")
user_input = st.text_input("Enter some text:")
if user_input:
    st.write("You entered:", user_input)
