import streamlit as st
import numpy as np
import pandas as pd

"""
# Uber Pickups Exercise
"""

DATA_URL  = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache(allow_output_mutation=True)
def download_data():
    return pd.read_csv(DATA_URL)

nrow = st.sidebar.slider("No. rows to display: ", 0, 10000, value = 1000)

hour_range = st.sidebar.slider("Select hour_range", 0, 24, (8,17))

st.sidebar.write("Hours selected: ", hour_range[0], hour_range[1])

data = (download_data()
        .rename(columns={"Date/Time": "date_time", "Lat": "lat", "Lon" : "lon", "Base": "base"})
        .assign(date_time = lambda df: pd.to_datetime(df.date_time))
        .loc[lambda df: (df.date_time.dt.hour >= hour_range[0]) & (df.date_time.dt.hour <= hour_range[1])]
        .loc[1:nrow]
        .sort_values("date_time", ascending=True)
        )

data

"""
## Uber Pickups Locations
"""
st.map(data)

"""
## Uber Pickups by Hour
"""
hist_values = pd.DataFrame(np.histogram(data.date_time.dt.hour, bins=24, range=(0,24))[0], columns=["Pickups"])
st.bar_chart(hist_values)