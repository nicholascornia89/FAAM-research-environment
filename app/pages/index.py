import streamlit as st

st.html("""<img src="app/static/faam-logo_gold.png" width="400" heigth="200">""")

st.write(
    """The Dutch word faam can be translated into celebrity, a suited name for the Flemish Archive for Annotated Music, a database and research platform aiming to revive the performances of musicians from the 19th and early 20th century through the study of their annotations on music scores.
The aim of this project is to create a digital research platform that will provide researchers and performers alike with an interactive corpus of annotated scores, supporting the artistic and academic question of how musicians of the pre-recording era performed their music. These annotations are part of the broad collection of the Heritage Library of the Royal Conservatoire Antwerp, acquired mostly from donations of musician’s relatives in the last several decades.
Tracing and making the annotations of performers widely available, conductors and composers of our past can help us better understand the relationship between written and sounding music, where the additional handwritten comments play a crucial role to bridge the gap between notation and performance. The project emphasizes the recent trends in the Historical Informed Practice movement, shifting the focus from composer’s written scores to the study of the act of performance in its broad cultural context.
The aim is to allow the scalability of the project for future integration of musical collections coming from other libraries in Flanders, such as those from conservatories and opera houses. This project wishes to provide a ground-truth for future digitization projects in music, opening the doors for 21st century musicology in the digital era."""
)

st.markdown(
    """
    ## Principal Investigator
    Nicholas Cornia \n
    Royal Conservatoire of Antwerp, Labo XIX&XX (2023-2025) \n
    *nicholas.cornia[at]ap.be*
    
    """
)

left_column, right_column = st.columns(2)


left_column.html(
    """<a href="https://ap-arts.be/en/researchgroup/labo-xixxx"><img src="app/static/Logo_LaboXIX&XX_gold.png" width="300" heigth="100"></a>"""
)

right_column.html(
    """<a href="https://ap-arts.be/koninklijk-conservatorium-antwerpen"><img src="app/static/rca_logo_gold.png" width="300" heigth="100"></a>"""
)
