import streamlit as st
import os

# Define the pages
pages = []
pages.append(st.Page(os.path.join("pages", "index.py"), title="Project"))
pages.append(st.Page(os.path.join("pages", "data_model.py"), title="Data Model"))
pages.append(st.Page(os.path.join("pages", "properties.py"), title="Properties"))
pages.append(st.Page(os.path.join("pages", "entities.py"), title="Entities"))
pages.append(
    st.Page(os.path.join("pages", "data_visualization.py"), title="Data Visualization")
)
pages.append(st.Page(os.path.join("pages", "export.py"), title="Export Data"))
# Set up navigation
pg = st.navigation(pages)

# Run the selected pages
pg.run()
