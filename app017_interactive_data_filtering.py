import streamlit as st
import pandas as pd

st.title("Interactive Data Filtering")

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 30, 22, 29, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
})

age_filter = st.slider("Filter by age", min_value=20, max_value=40, value=(20, 35))
filtered_data = data[(data["Age"] >= age_filter[0]) & (data["Age"] <= age_filter[1])]

st.write("Filtered Data:")
st.dataframe(filtered_data)
