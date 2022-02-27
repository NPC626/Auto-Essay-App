import streamlit as st
import pandas as pd

from sklearn.externals import joblib

generator = joblib.load('path.x')

st.write("""
# Auto-Essay App
This app produces a essay for the given keywords!
""")
st.write('---')

# Loads the Boston House Price Dataset
# boston = datasets.load_boston()
# X = pd.DataFrame(boston.data, columns=boston.feature_names)
# Y = pd.DataFrame(boston.target, columns=["MEDV"])

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    LEN = st.sidebar.slider('LEN', 10, 10000)
    data = LEN

    return LEN

text_len = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specify Input parameters')
st.text_input("Your phrase", key="phrase_input")
prompt = st.session_state.phrase_input
# prompt = "The chernobyl disaster" # Third line
res = generator(prompt, max_length= text_len, do_sample=True, temperature=0.9) # Fourth line
