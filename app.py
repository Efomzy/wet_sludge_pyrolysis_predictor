import streamlit as st
import pickle
import numpy as np
from xgboost import XGBRegressor
XGB1 = pickle.load(open('XGB1.pkl', 'rb'))
XGB2 = pickle.load(open('XGB2.pkl', 'rb'))
XGB3 = pickle.load(open('XGB3.pkl', 'rb'))
XGB4 = pickle.load(open('XGB4.pkl', 'rb'))
XGB5 = pickle.load(open('XGB5.pkl', 'rb'))
XGB6 = pickle.load(open('XGB6.pkl', 'rb'))
XGB7 = pickle.load(open('XGB7.pkl', 'rb'))

st.write('# Wet Sludge Pyrolysis Predictor')
st.subheader('(Ultimate and Proximate analysis should be in dry basis)')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
  C = st.number_input("Carbon content (%)", 0.00,50.00)

with col2:
  O = st.number_input("Oxygen content (%)", 0.00,35.00)
  
with col3:
  S = st.number_input("Sulfur content (%)", 0.00,20.00)
  
with col4:
  VM = st.number_input("Volatile Matter (%)", 0.00,75.00)
 
with col5:
  MC = st.number_input("Moisture Content (%)", 0.00,84.20)
  
with col1:
  H = st.number_input("Hydrogen content (%)", 0.00,15.00)

with col2:
  N = st.number_input("Nitrogen content (%)", 0.00,10.00)
  
with col3:
  A = st.number_input("Ash content (%)", 0.00,75.00)

with col4:
  FC = st.number_input("Fixed Carbon (%)", 0.00,20.00)

with col5:
  T = st.number_input("Temperature (°C)", 350,1000)
 

if C+H+O+N+S+A >= 95 and C+H+O+N+S+A <= 105 and A+VM+FC >= 95 and A+VM+FC <= 105:

  Biooil1 = XGB1.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  Syngas2 = XGB2.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  Biochar3 = XGB3.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  H24 = XGB4.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  CO5 = XGB5.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  CO26 = XGB6.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  CH47 = XGB7.predict([[C, H, O, N, S, A, VM, FC, MC, T]])
  Biooil = round(Biooil1[0], 2)
  Syngas = round(Syngas2[0], 2)
  Biochar = round(Biochar3[0], 2)
  H2 = round(H24[0], 2)
  CO = round(CO5[0], 2)
  CO2 = round(CO26[0], 2)
  CH4 = round(CH47[0], 2)
else:
  
  Biooil = 'error in input data'
  Syngas = 'error in input data'
  Biochar = 'error in input data'
  H2 = 'error in input data'
  CO = 'error in input data'
  CO2 = 'error in input data'
  CH4 = 'error in input data'

if st.button('Click here to predict sludge pyrolysis products'):
  col1, col2, col3, col4 = st.columns(4)
  with col1:
    st.write('Biooil (wt.%)', Biooil)
    
  with col2:
    st.write('Biochar (wt.%)', Biochar)
    
  with col3:
    st.write('CO (vol.%)', CO)
    
  with col4:
    st.write('CH4 (vol.%)', CH4)
    
  with col1:
    st.write('Syngas (wt.%)', Syngas)
    
  with col2:
    st.write('H2 (vol.%)', H2)
   
  with col3:
    st.write('CO2 (vol.%)', CO2)
    
    
