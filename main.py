# Imports
import streamlit as st
import random

# Code
st.title('HELLO ANDREJ!!!')
st.title(random.randint(1,100))

number1 = st.number_input('Insert a number', key=1, value=0)
number2 = st.number_input('Insert a number', key=2, value=0)

st.write('The current number is ', number1 + number2)