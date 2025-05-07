import streamlit as st

co1, co2 = st.columns([2, 3])
with co1 :
    st.title("here is  column1 title")

with co2:
    st.title("here is column2 title")
    st.checkbox("this is checkbox1 in co2")