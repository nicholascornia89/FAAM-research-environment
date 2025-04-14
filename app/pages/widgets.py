import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import json, csv

st.write("# Widgets")
st.write("## Slider")
x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)

st.divider()

st.write("## Text input")
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.write("You name is:", st.session_state.name)

st.write("## Selectboxes")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox(
    "Which number do you like best?", df["first column"], key="selectbox"
)

st.write("You selected: ", option, "which is the same as", st.session_state.selectbox)
