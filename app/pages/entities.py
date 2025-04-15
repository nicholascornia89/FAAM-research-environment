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


def get_knowledge_base(metadata_path):
	properties = json2dict(os.path.join(metadata_path, "properties.json"))
	data_model = json2dict(os.path.join(metadata_path, "data_model.json"))
	entities = json2dict(os.path.join(metadata_path, "entities.json"))
	return properties, data_model, entities


properties, data_model, entities = get_knowledge_base(metadata_path)

st.write("# Entities")

with st.expander("Filter Entities"):
	select_list = []
	for entity in entities.keys():
		select_list.append(f"{entity} | {entities[entity]["label"]}".replace("_", " ").capitalize())

	options = st.multiselect("Filter entities...", select_list)

	for selected in options:
		# convert back to _
		item = selected.replace(" ", "_").lower()
		st.write(f"## {selected}")
		df = pd.DataFrame(data_model[item]["statements"])
		st.dataframe(df)

with st.expander("Create new Entity"):
	# select data model schema
	select_list = []
	for data_type in data_model.keys():
		select_list.append(data_type.replace("_", " ").capitalize())

	data_model_schema = st.selectbox("Choose data model schemas", select_list).replace(" ","_").lower()

	with st.form("new_entity"):
		statements = []
		last_entity = len(list(entities.keys()))
		st.write(f"### New entity E{last_entity+1}")
		for p in data_model[data_model_schema]["statements"]:
			st.write(f"#### {p["label"].replace("_"," ")}")
			p_structure = properties[p["property"]]
			if p_structure["type"] in ["string","URL"]:
				st.text_input("",key=p["property"])
			if p_structure["type"] == "item":
				# create a select box with qualifiers
				select_list = []
				for entity in entities.keys():
					select_list.append(f"{entity} | {entities[entity]["label"]}".replace("_", " ").capitalize())

				value = st.selectbox("",select_list,key=p["property"])

		# Every form must have a submit button.
		submitted = st.form_submit_button("Sumbit")
		if submitted:
			st.write("Sumbitted")
			# TO BE CONTINUED...



	# initialize values according to data model
	#if "new_entity" not in st.session_state:
		#st.session_state.new_entity = {}


