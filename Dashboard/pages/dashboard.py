import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.subheader("Titanic Data - Data Insights and Visualizations")  #subheading
st.markdown("Get all the insights as stats and visuals of Titanic data in this application here.")  #to add a description 

st.subheader("Dataset")

df = sns.load_dataset("titanic")  
st.dataframe(df) 

#Filters 
st.sidebar.header("Filter Options")

gender = st.sidebar.multiselect("Gender",
                                options=df['sex'].unique()) #to select multiple options - multiselect and unique() to get unique values

passenger = st.sidebar.multiselect("Passenger Class",
                                options=df['class'].unique())

min_age, max_age = st.sidebar.slider("Age",
                                      min_value=int(df['age'].min()),
                                      max_value=int(df['age'].max()),
                                      value=(int(df['age'].min()), int(df['age'].max())))  #to select range of values - slider

st.subheader("Visuals of Insights")

#Age Distribution

fig = px.histogram(df, x="age", title="Age Distribution", color="embarked")
st.plotly_chart(fig) 
st.markdown("This graph shows the dustribution of age of the people at the titanic ship.") 

fig = px.box(df, x='pclass', y='age', color='survived', title="Age wise Fare")
st.plotly_chart(fig)  

