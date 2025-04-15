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

st.write("# Properties")

with st.expander("Filter Properties"):
    select_list = []
    for p in properties.keys():
        select_list.append(f"{p} | {properties[p]["label"]})".replace("_", " ").capitalize())

    options = st.multiselect("Filter properties...", select_list)

    for selected in options:
        # convert back to _
        item = selected.split("|")[0][:-1]
        st.write(f"## {selected}")
        df = pd.DataFrame([properties[item]])
        st.dataframe(df)
