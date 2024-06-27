import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os 
#from dotenv import load_dotenv

# load_dotenv('.env')
openai_api_key = os.getenv('openai_api_key')



# template = """
#     You are an AI who is an expert at Meal prepping
#     Your goal is to:
#     - Generate recipes based on the selected options
#     - Generate an grocery list based on the generated recipes only

#     Please follow the following guidance and format while generating the recipes.

#     The response should have two main sections. First section for Meal Prep Recipes and the Second section for grocery list.


#     ## Ingredients
    
#     In this section list out the ingredients as a bulleted list
    
#     ## Instructions

#     In this section provide step by step instructions 

#     ## Notes

#     In this section call out anything important the user should know


#     Here is an example of a grocery list, please follow the same format and categories while generating the grocery list. If it does not fall under predefined categories list it under miscellaneous:

#     Fresh produce 

#     * Apples
#     * Bananas
#     * Avocados
#     * Cilantro 

#     Grains and Bread

#     * Rice
#     * Quinoa
#     * Pasta
#     * Wheat Bread

#     Meat/Protein

#     * Chicken
#     * Eggs
#     * Tofu
#     * Tempeh 
#     * Ground beef
#     * Ham 

#     Dairy 

#     * Butter
#     * Milk
#     * Sour cream 
#     * Cheese

#     Canned/Dried goods 

#     * Beans 
#     * Chickpea
#     * Soup
#     * Tuna 

#     Condiments/Spices

#     * Pepper
#     * Salt 
#     * Cumin 
#     * Mustard 
#     * Mayo

#     Oils/Vinegars

#     * Coconut oil
#     * Olive oil 
#     * Apple cider vinegar

    
#     Below are the selected options:
#     MEALS: {meal}
#     NUMBER OF DAYS: {num_days}
#     DIETARY RESTRICTION: {diet}
#     SERVINGS: {servings}
    
#     YOUR RESPONSE:
# """

template = """
    You are an AI who is an expert at Meal prepping
    Your goal is to:
    - Generate Meal prep ideas based on the selected options
    - Generate an grocery list with quantity based on the generated meal prep ideas only

    Please follow the following guidance and format while generating the recipes.

    The response should have two main sections. First section for Meal Prep ideas and the Second section for grocery list.
    
    The meal prep ideas section should only list the name of dishes based on the selection.

    The grocery list should generate a bulleted list of groceries along with quantity.

    
    Below are the selected options:
    MEALS: {meal}
    NUMBER OF DAYS: {num_days}
    DIETARY RESTRICTION: {diet}
    SERVINGS: {servings}
    
    YOUR RESPONSE:
"""






prompt = PromptTemplate(
    input_variables=["meal","num_days", "diet", "servings"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm
 
llm = load_LLM(openai_api_key=openai_api_key)


st.set_page_config(page_title="MealAmigo: Make Meal Prep Less Boring", page_icon=":knife_fork_plate:")
st.header("Meal Prep Ideas and Grocery list generator")

st.markdown('''Meal prep is boring and time consuming. Preparing a grocery list is a pain!! 
            This tool will kill two birds with one AI stone.  
            This tool is powered by [LangChain](https://www.langchain.com/), [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/) and was built by [Santosh Srivatsa](https://github.com/san-to-sh)''')


st.markdown('''### Make the following selections''')

col1, col2 = st.columns(2)

with col1:

    option_meal = st.multiselect(
        'Please select your meal',
        ('Breakfast','Lunch','Dinner'))
    
    option_num_days = st.selectbox(
        'Please select number of days',
        ('1','2','3','4','5','6','7'))
    

with col2:

    option_diet = st.selectbox(
        'Which of the following dietary restrictions applies to you?',
        ('Vegan', 'Vegetarian', 'Gluten Free', 'Pescatarian','Pescapescetarian', 'I eat everything'))
    
    option_servings_per_meal = st.selectbox(
        'Please select number of servings per meal',
        ('1','2','3','4'))
    

if (option_meal is not None) and (option_diet is not None) and (option_num_days is not None) and (option_servings_per_meal is not None):
    prompt_input = prompt.format(meal=option_meal,num_days=option_num_days,diet=option_diet,servings=option_servings_per_meal)
    formatted_meal_prep = llm(prompt_input)
    # st.write(type(formatted_meal_prep))
    st.write(formatted_meal_prep)
