import streamlit
import pandas

streamlit.header('Breakfast Menu')
streamlit.header('🍌🥭 Throw Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Throw some fruits:", list(my_fruit_list.index),['Banana','Grapes','Lime'])

# Display the table
streamlit.dataframe(my_fruit_list)

streamlit.text('Omega 3 & Blackberry Oatmeal Worms')
streamlit.text('Kale, Beetroot, Spinach & Rocket Milkshake')
streamlit.text('Well-Boiled Extra-Range Swan Eggs with Toasted Poppy Seeds')
