import streamlit as st
import numpy as np
import pandas as pd

# Título
st.title('This is my first app from Galileo Master!')

# Variables y escritura
x = 4
st.write(x, '^2 = ', x*x)

x = 4
x, ' square is', x*x

# Dataframes
st.write('This is a Data Frame example')
st.write(pd.DataFrame({
    'Colum A' : ['A', 'B', 'C', 'D', 'E'],
    'Column B' : [1, 2, 3, 4, 5]
}))

"""
# Title: This is a Title tag

This is other example for dataframes
"""

df = pd.DataFrame({
    'Colum A' : ['A', 'B', 'C', 'D', 'E'],
    'Column B' : [1, 2, 3, 4, 5]
})

df

"""
## Show me some graphs
"""

df_to_plot = pd.DataFrame(
    np.random.randn(20,3), columns = ['Column A', 'Column B', 'Column C']
)

st.line_chart(df_to_plot)

"""
## Let's plot
"""

df_lat_lon = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon']
)

st.map(df_lat_lon)

if st.checkbox('show dataframe'):
    df_lat_lon

"""
Let's try somw widgets


###  1. Slider
"""

x = st.slider('Select a value for X', min_value = 1, max_value = 100, value = 4)
y = st.slider('Select a power for X', min_value = 0, max_value = 5, value = 2)
st.write(x, '^', y,'=', x**y)

"""
### What about options
"""
option_list = range(1, 11)
option = st.selectbox('Which number do you like best?', option_list)

st.write('Your favorite number is ', option)

"""
## How about a progress bar
"""

import time

label = st.empty()
progress_bar = st.progress(0)

for  i in range(0,101):
    label.text(f'The value is: {i}%')
    progress_bar.progress(i)
    time.sleep(0.01)

'The wait is done!'

st.sidebar.write("THis is a sidebar")

option_side = st.sidebar.selectbox('Select a number', option_list)
st.sidebar.write('Your favorite number is ', option_side)

st.sidebar.write("Another slidebar")

another_slider = st.sidebar.slider('Select Range', 0.0, 100.0, (25.0,75.0))

st.sidebar.write('The range selectd is ', another_slider)
