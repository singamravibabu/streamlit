import streamlit as st
import json

st.title("Display JSON Data")

sample_json = {
    "name": "John Doe",
    "age": 30,
    "email": "john@example.com",
    "hobbies": ["reading", "traveling", "coding"]
}

st.json(sample_json)
