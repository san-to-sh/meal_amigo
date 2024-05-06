import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
# from dotenv import load_dotenv
import os 


st.set_page_config(page_title="MealAmigo: Make Meal Prep Less Boring", page_icon=":knife_fork_plate:")
st.header("Recepie and Grocery list generator")

st.markdown('''Meal prep is boring and time consuming. Preparing a grocery list is a pain!! 
            This tool will kill two birds with one AI stone.  
            This tool is powered by [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/) and was built by [Santosh Srivatsa](https://github.com/san-to-sh)''')



st.markdown('''### Make the following selections''')

col1, col2, col3 = st.columns(3)

with col1:
    option_category = st.selectbox(
        'Which category does this complaint fall under?',
        ('Returns','Refunds','Shipment issue'))
with col2:
    option_tone = st.selectbox(
        'Which tone would you like your email to have?',
        ('Formal', 'Informal'))
    
with col3:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British'))