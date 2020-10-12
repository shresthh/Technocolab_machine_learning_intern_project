import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image

pickle_in=open("final_model.pkl",'rb')
classifier=pickle.load(pickle_in)
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict(AGE,EDUCATION,MARRIAGE,PAY_1,LIMIT_BAL,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT6,BILL_AMT5):
    prediction=classifier.predict([[AGE,EDUCATION,MARRIAGE,PAY_1,LIMIT_BAL,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT6,BILL_AMT5]])
    print(prediction)
    return prediction



def main():
    st.title("credit card defaulter")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Credit card default </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    AGE = st.text_input("AGE","Type Here")
    EDUCATION = st.text_input("EDUCATION","Type Here")
    MARRIAGE = st.text_input("marriage","Type Here")
    PAY_1 = st.text_input("PAY_1","Type Here")
    LIMIT_BAL = st.text_input("LIMIT_1","Type Here")
    PAY_AMT1 = st.text_input("PAY AMOUNT 1","Type Here")
    PAY_AMT2 = st.text_input("PAY AMOUNT 2","Type Here")
    PAY_AMT3 = st.text_input("PAY AMOUNT 3","Type Here")
    PAY_AMT4 = st.text_input("PAY AMOUNT 4","Type Here")
    PAY_AMT5 = st.text_input("PAY AMOUNT 5","Type Here")
    PAY_AMT6 = st.text_input("PAY AMOUNT 6","Type Here")
    BILL_AMT1 = st.text_input("BILL_AMT1","Type Here")
    BILL_AMT2 = st.text_input("BILL_AMT2","Type Here")
    BILL_AMT3 = st.text_input("BILL_AMT3","Type Here")
    BILL_AMT4 = st.text_input("BILL_AMT4","Type Here")
    BILL_AMT5 = st.text_input("BILL_AMT5","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(AGE,EDUCATION,MARRIAGE,PAY_1,LIMIT_BAL,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT6,BILL_AMT5)
    st.success('The output is {}'.format(result))

    if __name__=='__main__':
        main()