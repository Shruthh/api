# -*- coding: utf-8 -*-
"""stream.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KigpXbVFr-8apkVJGKHvrIVMzm8onqdy
"""

import streamlit as st
import numpy as np
import joblib

st.markdown('## Iris_Species_Prediction')
sepal_length=st.number_input('sepal length{cm}')
sepal_width=st.number_input('sepal width(cm)')
petal_length=st.number_input('petal lengthcm')
petal_width=st.number_input('petaal width(cm)')

if st.button('predict') [
    model=joblib.load('iris_model.pkl')
    x=np.array([sepal_length,sepal_width,petal_length,petal_width])
    if any(x<=0):
      st.markdown('### Inputs must be greater than0')
    else:
    st.markdown(f'### Prediction is{model.predict([[sepal_length,sepal_width,petal_length,petal_width]])[0]}')


