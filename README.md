# Streamlit Library

## Introduction
Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. It allows you to turn data scripts into shareable web apps in minutes, without needing any front-end development experience.

## Purpose
The primary purpose of Streamlit is to simplify the process of creating interactive web applications for data analysis and machine learning. It is designed to be easy to use, allowing developers to focus on their data and algorithms rather than the intricacies of web development.

## Installation
To install Streamlit, you can use pip, the Python package installer. Open your terminal or command prompt and run the following command:

```bash
pip install streamlit
```

## Running a Streamlit App
Once Streamlit is installed, you can create a new Python script and start building your app. Here is a simple example:

### Example Code
Create a new file called `app.py` and add the following code:

```python
import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app.')

number = st.slider('Pick a number', 0, 100)
st.write('You selected:', number)
```

### Running the App
To run the app, navigate to the directory containing `app.py` in your terminal or command prompt and execute:

```bash
streamlit run app.py
```

This will start a local web server and open your default web browser to display the app.

## Illustrations
Here are some key features of Streamlit with examples:

### Displaying Data
You can easily display data using Streamlit's built-in functions:

```python
import streamlit as st
import pandas as pd

data = {
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

st.write('DataFrame:')
st.dataframe(df)
```

### Interactive Widgets
Streamlit provides various interactive widgets like sliders, buttons, and text inputs:

```python
import streamlit as st

name = st.text_input('Enter your name')
st.write('Hello,', name)

if st.button('Click me'):
    st.write('Button clicked!')
```

### Plotting
You can also create and display plots using libraries like Matplotlib or Plotly:

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)
```

## Conclusion
Streamlit is a powerful tool for creating interactive web applications with minimal effort. It is particularly useful for data scientists and machine learning practitioners who want to share their work with others in an interactive format.