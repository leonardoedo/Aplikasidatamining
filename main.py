import streamlit as st
from web import load_data

from Tabs import home, Predict, Visualise

Tabs = {
    "Home" : home, 
    "Prediction" : Predict,
    'visualisasion' : Visualise
}

st.sidebar.title("navigasi")

page = st.sidebar.radio("pages", list(Tabs.keys()))

#load dataset
df, x,y = load_data()

#kondisi call app fuction

if page in ["Prediction", "visualisasion"]:
    Tabs[page].app(df, x,y)
else:
    Tabs[page].app()