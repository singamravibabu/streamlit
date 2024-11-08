import streamlit as st

st.title("Simple Survey Form")

name = st.text_input("What is your name?")
age = st.number_input("How old are you?", min_value=0, max_value=120)
feedback = st.text_area("Share your feedback:")
submit = st.button("Submit")

if submit:
    st.write("Thank you for your response, ", name, "!")
    st.write("Age:", age)
    st.write("Feedback:", feedback)
