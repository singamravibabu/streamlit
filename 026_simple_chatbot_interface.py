import streamlit as st

st.title("Simple Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")
if st.button("Send"):
    # Simple mock response
    response = f"Echo: {user_input}"
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.experimental_rerun()

st.write("## Chat History")
for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}**: {message}")
