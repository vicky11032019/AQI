import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("aqi_model.pickle", "rb")
aqi_reg=pickle.load(pickle_in)

def main():
    st.title("Air Quality Index Prediction")
    avg_temp=st.text_input("Average Temp (°C)", "type here")
    max_temp=st.text_input("Maximum Temp (°C)", "type here")
    min_temp=st.text_input("Minimum Temp (°C)", "type here")
    h= st.text_input("Humidity (%)", "type here")
    pp = st.text_input("Total Rainfall(in mm)", "type here")
    vv = st.text_input("Average Visibility(in KM)", "type here")
    v = st.text_input("Average wind speed (Km/h)", "type here")
    vm = st.text_input("Maximum sustained wind speed (Km/h)", "type here")

    result=""
    if st.button("Predict"):
        result=pred_aqi(avg_temp, max_temp, min_temp, h, pp, vv, v, vm)
    st.success('The AQI Index is {}'.format(result))

def pred_aqi(avg_temp, max_temp, min_temp, h, pp, vv, v, vm):
    prediction=aqi_reg.predict([[avg_temp, max_temp, min_temp, h, pp, vv, v, vm]])
    print(prediction)
    return prediction


if __name__=='__main__':
    main()


