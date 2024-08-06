# pip install -r requirements.txt
# python -m streamlit run your_script.py

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import numpy as np
import streamlit as st
import pandas as pd

st.title("Toronto Neighbourhood Demographics")
st.write("An interactive website that lets users to extract data from https://open.toronto.ca/dataset/neighbourhood-profiles/.")
st.write("If more details are needed, email me at bensonyan778@hotmail.com for suggestions")
st.write("note that neighbourhood 104 Lawrence Phttps://open.toronto.ca/dataset/neighbourhood-profiles/ark South is unavailable")
df = pd.read_csv("./neighbourhood-profiles-2021.csv", encoding='latin-1')
df

neighbourhood = st.selectbox("choose neighbourhood", ("1", "2", "3"))


dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))