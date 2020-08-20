import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in = open("regressor.pkl","rb")
reg = pickle.load(pickle_in)

def predictions(hours):
	prediction = reg.predict([[hours]])
	print(prediction)
	return prediction

def main():
	st.title("Student Score")

	html_temp = """
	<div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Student Score ML App </h2>
    </div>
	"""

	st.markdown(html_temp,unsafe_allow_html=True)
	result=""

	hrs = st.number_input("Hours of Study")

	if st.button("Predict"):
		result = predictions(hrs)
	st.success('The output is {}'.format(result))

if __name__=='__main__':
	main()