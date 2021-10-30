import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

"""
# Uber pickups Exercise
"""

DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


@st.cache(allow_output_mutation=True)
def download_data(nrows):
    return pd.read_csv(DATA_URL, nrows=nrows)


def hours(data):
    return pd.DataFrame({'hour': data['date_time'].dt.hour})


nrow = st.sidebar.slider('No. rows to display', 0, 1000, value=1000)
hour_range = st.sidebar.slider('Select the hour range', 0, 24, (8, 17))

st.sidebar.write('Hour selected: ', hour_range[0], hour_range[1])

data = (download_data(100000)
        .rename(columns={'Date/Time': 'date_time', 'Lat': 'lat', 'Lon': 'lon', 'Base': 'base'})
        .assign(date_time=lambda df: pd.to_datetime(df.date_time))
        .loc[lambda df: (df.date_time.dt.hour >= hour_range[0]) & (df.date_time.dt.hour < hour_range[1])]
        .loc[1:nrow]
        .sort_values(by='date_time')
        )

data

st.map(data)

hours(data).hist()
plt.show()
st.pyplot()
