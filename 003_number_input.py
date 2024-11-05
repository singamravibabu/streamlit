import streamlit as st

st.title("Number Input Example")
number = st.number_input("Enter a number:", min_value=0, max_value=100)
st.write("The square of the number is:", number ** 2)
