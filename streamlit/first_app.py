
import streamlit as st
import numpy as np
import pandas as pd

st.title("This is my first app from Galileo Master")

x = 4
st.write(x, " square is ", x*x)
x, " square i s", x*x

st.write("This is a Data Frame example")
st.write(pd.DataFrame( {
    "Column A" : ["A", "B", "C", "D", "E"],
    "Column B" : [1, 2, 3, 4, 5]
}))

"""
# Title: This is Title tag
This is other example for dataframes
"""

df = st.write(pd.DataFrame( {
    "Column A" : ["A", "B", "C", "D", "E"],
    "Column B" : [1, 2, 3, 4, 5]
}))

df

"""
## Show me some graphs

"""

df_to_plot = pd.DataFrame(
    np.random.randn(20,3), columns= ["Column A", "Column B", "Column C"]
)

st.line_chart(df_to_plot)

"""
## Let's plot a map!
"""

def_lat_lon = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)

st.map(def_lat_lon)

"""
## Let's try some widgets
"""
x = st.slider("Select a value for X", min_value=1, max_value=100, value=4)
y = st.slider("Select a power of X", min_value=0, max_value=3, value=2)
st.write(x, "cube is", x**y )

"""
### What about options
"""
def test():
    st.write("Función ejecutada :)")

option_list = range(1,11)
option = st.selectbox("Which number do you like best?", option_list, on_change=test)

st.write("Your favorite number is: ", option)

"""
## How about a progress bar
"""

import time

label = st.empty()
progress_bar = st.progress(0)

for i in range(0, 101):
    label.text(f'The process is: {i}%')
    progress_bar.progress(i)
    time.sleep(0.01)

"The wait time is done"

option_side = st.sidebar.selectbox("Select a Side number", option_list)
st.sidebar.write("The selection is: ", option_side)

st.sidebar.write("Another slider")

another_slider = st.sidebar.slider("Select Range", 0.0, 100.0, (25.0, 75.0))
st.sidebar.write("The range selected is: ", another_slider)