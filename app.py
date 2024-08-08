# pip install -r requirements.txt
# python -m streamlit run app.py

import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
- [Selected Neighbourhood](#selected-neighbourhood)
- [Income](#income)
- [Family Demographics](#family-demographics)
- [Age Distribution](#age-distribution)
- [Labour Force](#labour-force)
- [Languages](#languages)
''', unsafe_allow_html=True)

# We can details from the first column (co  ntains age, salary, etc.)
column_0 = df["Neighbourhood Name"]
column_n = df[neighbourhood]

# we now use this new dataframe for future referenece
neighbourhood_df = pd.DataFrame({
    'Key Details': column_0,
    neighbourhood: column_n
})

st.header("Selected Neighbourhood", divider=True)
# Find the column number of the neighbourhood name.
column_number = df.columns.get_loc(neighbourhood)
st.write("Chosen neighbourhood is in column " + str(column_number) + " with the following stats:")
st.dataframe(neighbourhood_df, use_container_width=True)


# Age Section------------------------------------------------------------
st.header("Age", divider=True)
st.write("Age Distribution for Selected Neighborhood:")

# select rows 29-32
age_rows = neighbourhood_df.loc[[29, 30, 31, 32]]
# extract that column with selected neighbourhood
neighbourhood_age_column = age_rows[neighbourhood]
# get a list of 
labels = column_0[29:33]

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(neighbourhood_age_column, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'color': 'white'})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig.patch.set_alpha(0)

col1_age_distribution, col2_age_distribution = st.columns([1, 1])

col1_age_distribution.subheader("Age Distribution Pie Chart")
col2_age_distribution.subheader("Age Distrubtion Table")

col1_age_distribution.pyplot(fig)
col2_age_distribution.write(age_rows)



# income of individuals
# income adjusted with inflation
# Income compared to other neighbourhood rankings



st.header("Family Demographics", divider=True)
# Types of families (couple, family, etc.)
# # people in households
# Ethnicity




st.header("Age Distribution", divider=True)
# age





st.header("Labour Force", divider=True)





st.header("Languages", divider=True)




