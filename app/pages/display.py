import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import json, csv

st.write("# Display")
st.write("## Example with dataframes")
st.write(
    """
Here an example of a **string** with *italic*[^1] and some link to [Wikidata](www.wikidata.org). \n
Also a list
- [ ] unchecked
- [x] checked 

[^1]: Streamlit does not accept italic with _ 

"""
)

show_dataframe = st.checkbox("Show dataframe", key="dataframe")
if show_dataframe:
    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
    st.table(df)
    st.dataframe(df)


st.write("## Example adding charts and maps")

show_charts = st.checkbox("Show charts", key="charts")
if show_charts:
    # display in columns
    left_column, right_column = st.columns(2)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    left_column.line_chart(chart_data)
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    right_column.map(map_data)

st.write("# Example session state")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
