# Imports
import streamlit as st
import random

# Code
st.title('Uber pickups in USA')
st.title(random.randint(1,100))
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)