import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Exploration Data Analysis"
)

#Data Loading
database = pd.read_csv('Realtime-env2.csv')

# Drop Date and Time Column
database.drop(columns=['Date','Time'],inplace=True)
database.info()

st.header('Exploration Data Analysis')

# See number of unique data
st.subheader("Number of Unique Data")
st.bar_chart(database.nunique(),use_container_width=True)

# See the Mean of data
st.subheader("Average of Data")
st.bar_chart(database.mean(),use_container_width=True)

# See Correlation of each data
st.subheader("See Correlation of Each Data")
fig, ax = plt.subplots()
sns.heatmap(database.corr(method='kendall'), annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, ax=ax)

# Show the plot in Streamlit
st.pyplot(fig)