# Imports
import streamlit as st
import random

# Code
st.title('Uber pickups in USA')
st.title(random.randint(1,100))

number1 = st.number_input('Insert a number', key=1)
number2 = st.number_input('Insert a number', key=2)

st.write('The current number is ', number1 + number2)