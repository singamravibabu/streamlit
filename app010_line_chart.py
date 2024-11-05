import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart Example")
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(data)
