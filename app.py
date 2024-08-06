# pip install -r requirements.txt
# python -m streamlit run your_script.py

import numpy as np
import streamlit as st
import pandas as pd

st.title("Toronto Neighbourhood Demographics")
st.markdown("""
An interactive website that lets users extract data from [Toronto Neighbourhood Profiles Dataset](https://open.toronto.ca/dataset/neighbourhood-profiles/).
If more details are needed, email me at [bensonyan778@hotmail.com](mailto:bensonyan778@hotmail.com) for suggestions. Note that neighbourhood 104 Lawrence Park South is unavailable from the dataset.
""")

# Loading csv file for usage. encoding must be latin-1 
df = pd.read_csv("./neighbourhood-profiles-2021.csv", encoding='latin-1')
df

# Take all column names and place it into a list. Also remove 0'th element since it's called "Neighbourhood Name"
neighbourhood_names = df.columns.tolist()
neighbourhood_names.pop(0)

# The dropdown menu
neighbourhood = st.selectbox("Choose a neighbourhood", (neighbourhood_names))

# Find the column number of the neighbourhood name.
column_number = df.columns.get_loc(neighbourhood)
st.write("Chosen neighbourhood is in column number: " + str(column_number))

# We can details from the first column (contains age, salary, etc.)
column_0 = df["Neighbourhood Name"]
column_n = df[neighbourhood]

df_new = pd.DataFrame({
    'Key Details': column_0,
    'Neighbourhood Stats': column_n
})

st.write(df_new)