import streamlit as st
from datetime import datetime
import time

st.title("Live Time Display")

while True:
    st.write("Current Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(1)
    st.experimental_rerun()
