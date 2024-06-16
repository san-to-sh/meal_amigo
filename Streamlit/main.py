import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
# from dotenv import load_dotenv
import os 

template = """
    You are an AI who is an expert at Meal prepping
    Your goal is to:
    - Generate recipes based on the selected options
    - Generate an grocery list based on the generated recipes only

    Here is an example of a recipe, please follow the same format while generating recipes:

    Ingredients
    * 1 package of tempeh (8oz) -1/2 cup of balsamic vinegar (125mL)
    * 4 teaspoons tamari or soy sauce (20mL)
    * 1 tablespoon maple syrup (15mL)
    * 1 tablespoon olive oil (15mL)
    
    Instructions

    * Cut tempheh in to desired shape
    * In baking dish add all ingredients
    * Add tempeh and let marinade in fridge for a 2 to 12 hours. Toss tempeh a few times.
    * Preheat oven to 350C (180C)
    * Bake covered for 20 minutes
    * Remove cover, flip tempeh, and cook for 30 minutes
    * Remove from oven and let set to absorb marinade
    * Depending on baking dish size it is usually easier to double the recipe. Use this as protien replacement in dish where flavor profile fits or have as snacks.

    Notes

    you can get away with 2 hours of marinating but longer can be better if time permits. I have personally not been able to differentiate between like 6 and 12 hours. I usually prep this in morning and put it in fridge.
    might want make sure the dish is at roomish temperature before putting in oven.
    clean dish sooner than later
    Quick prep and only oven time for cooking. For a quick meal add some quinoa or wild rice with a vegetable of choice.

    Here is an example of a grocery list, please follow the same format and categories while generating the grocery list. If it does not fall under predefined categories list it under miscellaneous:

    Fresh produce 

    * Apples
    * Bananas
    * Avocados
    * Cilantro 

    Grains and Bread

    * Rice
    * Quinoa
    * Pasta
    * Wheat Bread

    Meat/Protein

    * Chicken
    * Eggs
    * Tofu
    * Tempeh 
    * Ground beef
    * Ham 

    Dairy 

    * Butter
    * Milk
    * Sour cream 
    * Cheese

    Canned/Dried goods 

    * Beans 
    * Chickpea
    * Soup
    * Tuna 

    Condiments/Spices

    * Pepper
    * Salt 
    * Cumin 
    * Mustard 
    * Mayo

    Oils/Vinegars

    * Coconut oil
    * Olive oil 
    * Apple cider vinegar

    
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
st.header("Recipe and Grocery list generator")

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
    

if (option_meal is not None) and (option_diet is not None) and (option_num_days is not None) and (option_servings_per_meal is not None):
    prompt_input = prompt.format(meal=option_meal,num_days=option_num_days,diet=option_diet,servings=option_servings_per_meal)
    formatted_meal_prep = llm(prompt_input)
    st.markdown(formatted_meal_prep)