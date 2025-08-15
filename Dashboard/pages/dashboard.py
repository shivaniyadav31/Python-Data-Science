import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.subheader("Titanic Data - Data Insights and Visualizations")  #subheading
st.markdown("Get all the insights as stats and visuals of Titanic data in this application here.")  #to add a description 

st.subheader("Dataset")

df = sns.load_dataset("titanic")  

#Filters 
st.sidebar.header("Filter Options")

gender = st.sidebar.multiselect("Gender",
                                options=df['sex'].unique(),
                                default = df['sex'].unique()) #to select multiple options - multiselect and unique() to get unique values

pclass = st.sidebar.multiselect("Passenger Class",
                                options=df['pclass'].unique(),
                                default = df['pclass'].unique())  #to select multiple options - multiselect and unique() to get unique values

min_age, max_age = st.sidebar.slider("Age",
                                      min_value=int(df['age'].min()),
                                      max_value=int(df['age'].max()),
                                      value=(int(df['age'].min()), int(df['age'].max())))  #to select range of values - slider

filtered_data = df[
    (df['sex'].isin(gender))&
    (df['pclass'].isin(pclass))&
    (df['age'] >= min_age)&
    (df['age'] <= max_age)
]
st.dataframe(filtered_data)  #to display the filtered data in a table format
st.subheader("Visuals of Insights")

#Age Distribution

fig = px.histogram(filtered_data, x="age", title="Age Distribution", color="embarked")
st.plotly_chart(fig) 
st.markdown("This graph shows the dustribution of age of the people at the titanic ship.") 

fig = px.box(filtered_data, x='pclass', y='age', color='survived', title="Age wise Fare")
st.plotly_chart(fig) 
st.markdown("This graph shows the age wise fare of the people at the titanic ship.") 

fig = px.violin(filtered_data, x='sex', y='age', color='survived', box=True, points='all', title='Violin Plot of Age by Sex and Survival')
st.plotly_chart(fig)
st.markdown("This graph shows the Violin Plot of Age by Sex and Survival of the people at the titanic ship.")

fig = px.scatter(filtered_data, x='age', y='fare', color='survived', symbol='sex', title="Age vs Fare by Survival", hover_data=['pclass', 'embarked'])
st.plotly_chart(fig)
st.markdown("This graph shows the scatter plot of Age vs Fare by Survival of the people at the titanic ship.")

fig = px.sunburst(filtered_data, path=['pclass', 'sex', 'survived'], values='fare', color='survived', title="Sunburst Chart: Class, Sex, and Survival")
st.plotly_chart(fig)
st.markdown("This graph shows the Sunburst Chart of Class, Sex and Survival of the people at the titanic ship.")

avg_fare = filtered_data.groupby('pclass')['fare'].mean().reset_index()
fig = px.bar(avg_fare, x='pclass', y='fare', title="Average Fare by Passenger Class", labels={'fare': 'Average Fare', 'pclass': 'Passenger Class'})
st.plotly_chart(fig)
st.markdown("This graph shows the Average Fare by Passenger Class of the people at the titanic ship.")

survival_gender = filtered_data.groupby('sex')['survived'].mean().reset_index()
fig = px.pie(survival_gender, values='survived', names='sex', title="Survival Rate by Gender", hole=0.4)
st.plotly_chart(fig)
st.markdown("This graph shows the Survival Rate by Gender of the people at the titanic ship.")

age_fare = filtered_data.groupby('age')['fare'].mean().reset_index()
fig = px.line(age_fare, x='age', y='fare', title="Average Fare by Age")
st.plotly_chart(fig)
st.markdown("This graph shows the Average Fare by Age of the people at the titanic ship.")

survivors_by_class = filtered_data.groupby(['pclass', 'survived']).size().reset_index(name='count')
fig = px.bar(survivors_by_class, x='pclass', y='count', color='survived', barmode='group', title="Survivors by Passenger Class")
st.plotly_chart(fig)
st.markdown("This graph shows the Survivors by Passenger Class of the people at the titanic ship.")

st.subheader("Conclusion")
st.markdown("This dashboard provides insights into the Titanic dataset, showcasing the demographics, survival rates, and other key statistics of passengers. The visualizations help in understanding the impact of factors like age, gender, and passenger class on survival rates. The interactive filters allow users to explore the data based on their preferences, making it easier to draw conclusions about the passengers of the Titanic.")  #to add a conclusion
