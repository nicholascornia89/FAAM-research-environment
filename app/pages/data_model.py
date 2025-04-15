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


properties, data_model = get_data_model(metadata_path)

st.write("# Data Model")

with st.expander("Filter Data Model"):
    select_list = []
    for data_type in data_model.keys():
        select_list.append(data_type.replace("_", " ").capitalize())

    options = st.multiselect("Filter data model schemas...", select_list)

    for selected in options:
        # convert back to _
        item = selected.replace(" ", "_").lower()
        st.write(f"## {selected}")
        df = pd.DataFrame(data_model[item]["statements"])
        st.dataframe(df)
