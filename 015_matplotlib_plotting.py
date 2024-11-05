import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Matplotlib Plot in Streamlit")

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

st.pyplot(fig)
