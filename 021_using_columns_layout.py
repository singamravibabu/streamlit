import streamlit as st

st.title("Using Columns for Layout")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Content in column 1")

with col2:
    st.header("Column 2")
    st.write("Content in column 2")

with col3:
    st.header("Column 3")
    st.write("Content in column 3")
