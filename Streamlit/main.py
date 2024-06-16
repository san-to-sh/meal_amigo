import streamlit as st
# from langchain import PromptTemplate
# from langchain.llms import OpenAI
# from dotenv import load_dotenv
import os 


st.set_page_config(page_title="MealAmigo: Make Meal Prep Less Boring", page_icon=":knife_fork_plate:")
st.header("Recepie and Grocery list generator")

st.markdown('''Meal prep is boring and time consuming. Preparing a grocery list is a pain!! 
            This tool will kill two birds with one AI stone.  
            This tool is powered by [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/) and was built by [Santosh Srivatsa](https://github.com/san-to-sh)''')



st.markdown('''### Make the following selections''')

col1, col2 = st.columns(2)

with col1:

    option_meal = st.multiselect(
        'Please select your meal',
        ('Breakfast','Lunch','Dinner'))
    
    option_num_days = st.multiselect(
        'Please select number of days',
        ('1','2','3','4','5','6','7'))
    

with col2:

    option_diet = st.selectbox(
        'Which of the following dietary restrictions applies to you?',
        ('Vegan', 'Vegetarian', 'Gluten Free', 'Pescatarian','Pescapescetarian', 'I eat everything'))
    
    option_servings_per_meal = st.multiselect(
        'Please select number of servings per meal',
        ('1','2','3','4'))
    

    

    
