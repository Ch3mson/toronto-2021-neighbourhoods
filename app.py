# pip install -r requirements.txt
# python -m streamlit run app.py

import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Toronto Neighbourhood Demographics (2021) ")
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
- [Age](#age)   
- [Family Demographics](#family-demographics)
- [Income Distribution](#income-distribution)
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


# Age Distribution Section ------------------------------------------------------------
st.header("Age", divider=True)

# take necessary rows containing age information
# extract that column with selected neighbourhood
# get a list of labels
age_rows = neighbourhood_df.loc[[3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
age_numbers = neighbourhood_df.loc[[3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]][neighbourhood]
labels = column_0.loc[[3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

# Create a pie chart with transparent background
fig, ax = plt.subplots()
ax.pie(age_numbers, labels=labels, autopct='%1.1f%%', textprops={'color': 'white'})
ax.axis('equal')
fig.patch.set_alpha(0)

# Displaying chart and table in 2 columns
col1_age_distribution, col2_age_distribution = st.columns([1.5, 1])
col1_age_distribution.subheader("Age Distribution Pie Chart")
col2_age_distribution.subheader("Age Distrubtion Table")
col1_age_distribution.pyplot(fig)
col2_age_distribution.write(age_rows)
st.write("Average age: " + neighbourhood_df[neighbourhood][33])
st.write("Median age: " + neighbourhood_df[neighbourhood][34])

# Family Demographics Section ------------------------------------------------------------
st.header("Family Demographics", divider=True)
# Types of families (couple, family, etc.)
family_demographic_children_rows = neighbourhood_df.loc[[233, 234, 235]]
family_demographic_children_numbers = neighbourhood_df.loc[[233, 234, 235]][neighbourhood].tolist()
# convert labels to list and remove initial spaces. Convert strings to int for numbers
family_demographic_children_labels = column_0.loc[[233, 234, 235]].tolist()
family_demographic_children_labels = [item.strip() for item in family_demographic_children_labels]
family_demographic_children_numbers = list(map(int, family_demographic_children_numbers))

fig1, ax = plt.subplots()

ax.bar(family_demographic_children_labels, family_demographic_children_numbers, label=family_demographic_children_labels, width=0.5)
ax.set_ylabel('Population')
ax.set_title("Families with Children")

percent_children = family_demographic_children_numbers[1] / family_demographic_children_numbers[0] * 100
percent_no_children = family_demographic_children_numbers[2] / family_demographic_children_numbers[0] * 100

# people in households
people_in_households = neighbourhood_df.loc[[224, 225, 226, 227, 228, 229]]
people_in_households_numbers = neighbourhood_df.loc[[224, 225, 226, 227, 228, 229]][neighbourhood].tolist()
people_in_households_labels = column_0.loc[[224, 225, 226, 227, 228, 229]].tolist()
people_in_households_labels = [item.strip() for item in people_in_households_labels]
people_in_households_labels[0] = 'Sample Total'
people_in_households_labels[5] = '5+ persons'
people_in_households_numbers = list(map(int, people_in_households_numbers))

fig2, ax = plt.subplots()
ax.bar(people_in_households_labels, people_in_households_numbers, label=people_in_households_labels, width=0.5)
ax.set_ylabel('Number of Households')
ax.set_title("Household Size Distribution")
plt.tight_layout()
col1, col2 = st.columns([1, 1])

col1.subheader("Families with Children")
col2.subheader("Household Size")
col1.pyplot(fig1)
col2.pyplot(fig2)
col1.write(family_demographic_children_rows)
col2.write(people_in_households)
st.write(f"% families with children: {percent_children:.2f}%")
st.write(f"% families with no children: {percent_no_children:.2f}%")

# Income Distribution Section ------------------------------------------------------------
st.header("Income Distribution", divider=True)
income_distribution = neighbourhood_df.loc[[92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 103, 104]]
income_distribution_numbers = neighbourhood_df.loc[[92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 103, 104]][neighbourhood].tolist()
income_distribution_labels = column_0.loc[[92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 103, 104]].tolist()
income_distribution_labels[0] = 'Under $10,000'
income_distribution_labels[11] = '$150,000+'
income_distribution_numbers = list(map(int, income_distribution_numbers))

fig, ax = plt.subplots()
ax.bar(income_distribution_labels, income_distribution_numbers, label=income_distribution_labels, width=0.5)
ax.set_ylabel('Income')
ax.set_title('Income Distribution of ' + neighbourhood)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.subheader("Total income groups in 2020 for the population aged 15 years and over in private households - 25% sample data")
st.write(fig)
st.dataframe(income_distribution, use_container_width=True)
st.write("Median income: $" + neighbourhood_df[neighbourhood][140])
st.write("Median income: $" + neighbourhood_df[neighbourhood][141])
# Income compared to other neighbourhood rankings





# Labour Force Section ------------------------------------------------------------
st.header("Labour Force", divider=True)




# Languages Section ------------------------------------------------------------
st.header("Languages", divider=True)




