import streamlit as st

st.title("Using Sidebar Widgets")
sidebar_option = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", sidebar_option)
