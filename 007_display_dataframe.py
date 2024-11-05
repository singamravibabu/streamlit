import streamlit as st
import pandas as pd

st.title("Displaying a DataFrame")
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
st.write("Here is a simple DataFrame:")
st.dataframe(df)
