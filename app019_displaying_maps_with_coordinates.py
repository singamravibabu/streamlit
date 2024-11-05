import streamlit as st
import pandas as pd

st.title("Displaying a Map")

data = pd.DataFrame({
    "latitude": [37.7749, 34.0522, 40.7128],
    "longitude": [-122.4194, -118.2437, -74.0060]
})

st.map(data)
