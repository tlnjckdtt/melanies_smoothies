# Import python packages
import streamlit as st
# from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests

# Write directly to the app
st.title(f":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
  """Choose the fruit you want in your custom smoothie!
  """
)
# option=st.selectbox('What is your favorite food?',('Banana','Strawberries','Peaches'))
# st.write('Your favorite fruit is: ', option)

name_on_order = st.text_input('Name on Smoothie: ')
st.write('The name on your Smoothie will be: ', name_on_order)

#session = get_active_session()
cnx=st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'),col('SEARCH_ON'))
st.dataframe(data=my_dataframe, use_container_width=True)
st.stop()



