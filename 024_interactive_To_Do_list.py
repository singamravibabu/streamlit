import streamlit as st

st.title("Interactive To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    st.session_state.tasks.append(new_task)
    st.experimental_rerun()

st.write("## Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    st.write(f"{i + 1}. {task}")
