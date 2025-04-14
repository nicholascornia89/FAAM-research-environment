import streamlit as st
import json, csv
from time import gmtime, strftime
import os
import pandas as pd

# I am assuming to run the script from root directory
import sys

sys.path.append("./modules")  # importing custom functions in modules
from modules.utilities import *

metadata_path = "./metadata"


def get_data_model(metadata_path):
    properties = json2dict(os.path.join(metadata_path, "properties.json"))
    data_model = json2dict(os.path.join(metadata_path, "data_model.json"))
    return properties, data_model


def show_button_list_data_model(data_model, properties):
    for data_type in data_model.keys():
        name = data_type.replace("_", " ").capitalize()
        if left_column.button(name, key=data_type):
            # show statements on right side
            right_column.write(f"## {name}")
            df = pd.DataFrame(data_model[data_type]["statements"])
            right_column.dataframe(df, use_container_width=True)


properties, data_model = get_data_model(metadata_path)

st.write("# Data Model")

left_column, right_column = st.columns(2)

show_button_list_data_model(data_model, properties)

st.write("# Properties")

st.markdown("**To be continued...**")
