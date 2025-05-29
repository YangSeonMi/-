import streamlit as st

st.title('title')
st.header('this is header')
st.subheader('this is subheader')

co1, co2 = st.columns([2, 3])
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])
tab3 = st.tabs(['Tab C'])

with co1 :
    st.title("here is  column1 title")
    with tab1:
        st.write("hello")
    with tab2:
        st.write("hi")
    with tab2:
        st.write("help")
    with tab3:
        st.write("I'm want go home")


with co2:
    st.title("here is column2 title")
    st.checkbox("this is checkbox1 in co2")
    st.checkbox("this is checkbox2 in co2")
    st.checkbox("this is checkbox3 in co2")

co1.subheader("I am solumn1 subheader")
co2.checkbox("this i checkbox2 in co2")