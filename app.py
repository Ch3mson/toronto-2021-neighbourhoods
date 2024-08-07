# pip install -r requirements.txt
# python -m streamlit run app.py

import numpy as np
import streamlit as st
import pandas as pd

st.title("Toronto Neighbourhood Demographics")
st.markdown("""
An interactive website that lets users extract data from [Toronto Neighbourhood Profiles Dataset](https://open.toronto.ca/dataset/neighbourhood-profiles/).
If more details are needed, email me at [bensonyan778@hotmail.com](mailto:bensonyan778@hotmail.com) for suggestions. Note that neighbourhood 104 Mount Pleasant West is unavailable from the dataset.
""")

# Loading csv file for usage. encoding must be latin-1 
df = pd.read_csv("./neighbourhood-profiles-2021.csv", encoding='latin-1')
df

# Take all column names and place it into a list. Also remove 0'th element since it's called "Neighbourhood Name"
neighbourhood_names = df.columns.tolist()
neighbourhood_names.pop(0)

# selected neighbourhood with sidebar
neighbourhood = st.sidebar.selectbox(
    "Select a neighbourhood",
    neighbourhood_names
)

st.sidebar.markdown('''
# Sections
- [Income](#income)
- [Family Demographics](#family-demographics)
- [Age Distribution](#age-distribution)
- [Labour Force](#labour-force)
- [Languages](#languages )
''', unsafe_allow_html=True)

# Find the column number of the neighbourhood name.
column_number = df.columns.get_loc(neighbourhood)
st.write("Chosen neighbourhood is in column " + str(column_number) + " with the following stats:")

# We can details from the first column (contains age, salary, etc.)
column_0 = df["Neighbourhood Name"]
column_n = df[neighbourhood]

df_new = pd.DataFrame({
    'Key Details': column_0,
    neighbourhood: column_n
})


st.dataframe(df_new, use_container_width=True)

st.header("Income", divider=True)
st.header("Family Demographics", divider=True)
st.header("Age Distribution", divider=True)
st.header("Labour Force", divider=True)
st.header("Languages", divider=True)