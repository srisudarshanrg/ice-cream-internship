import streamlit as st

def sidebar_component():
    with st.sidebar:
        st.title("Ice Cream Internship")
        return st.radio(label="", options=["Home", "Age Flavour Recommender", "Sales Predictor"])
