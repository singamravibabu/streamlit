import streamlit as st
import pandas as pd

st.title("File Download Example")

# Create sample data
data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
})

# Convert to CSV
csv = data.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, "data.csv", "text/csv")
