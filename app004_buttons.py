import streamlit as st

st.title("Interactive Buttons")
if st.button("Click Me"):
    st.write("Button clicked!")
else:
    st.write("Click the button to see what happens.")
