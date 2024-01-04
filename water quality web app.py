# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:54:22 2022

@author: RASIKA KAMBLI
"""

import numpy as np
import pickle
import streamlit as st
 
loaded_model = pickle.load(open(r'C:\Users\RASIKA KAMBLI\Desktop\Sem 3\Water\trained_model.sav','rb'))

def water_quality_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
       return'Water is not Drinkable'
    else:
       return'Water is  Drinkable'
       
       
def main():
    st.title('Water Quality Prediction')
    col1, col2, col3 = st.columns(3)
    
    with col1:
       ph = st.text_input('Please Enter pH value:')
        
    with col2:
         Hardness = st.text_input('Please Enter Hardness value:')
    
    with col3:
        Solids = st.text_input('Please Enter Solids value:')
    
    with col1:
        Chloramines = st.text_input('Please Enter Chloramines value:')
    
    with col2:
        Sulfate = st.text_input('Please Enter Sulfate value:')
    
    with col3:
         Conductivity = st.text_input('Please Enter Conductivity value:')
    
    with col1:
         Organic_carbon = st.text_input('Please Enter Organic_carbon value:')
    
    with col2:
        Trihalomethanes = st.text_input('Please Enter Trihalomethanes value:')
   
    with col3:
        Turbidity = st.text_input('Please Enter Turbidity value:')
   
    diagnosis =''
    
    if st.button('Water Quality Result'):
        diagnosis = water_quality_prediction(
            [ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()