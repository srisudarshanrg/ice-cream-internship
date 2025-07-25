import streamlit as st
from components import sidebar
from pages import home, age_flavour_chatbot, sales_predictor

st.markdown(
    """
        <style>
            [data-testid="stSidebar"] {
                min-width: 20%;
                max-width: 20%;
            }
        </style>
    """, unsafe_allow_html=True
)

page = sidebar.sidebar_component()

if page == "Home":
    home.home()
elif page == "Age Flavour Recommender":
    age_flavour_chatbot.age_flavour_chatbot()
elif page == "Sales Predictor":
    sales_predictor.sales_predictor()