import streamlit as st

st.title("Multi-Page Streamlit App")

# Sidebar for navigation
page = st.sidebar.selectbox("Choose a page:", ["Home", "About", "Contact"])

if page == "Home":
    st.subheader("Welcome to the Home Page!")
    st.write("This is the main content of the Home page.")
elif page == "About":
    st.subheader("About Us")
    st.write("This page contains information about our app.")
elif page == "Contact":
    st.subheader("Contact Us")
    st.write("Here are the details to get in touch with us.")
