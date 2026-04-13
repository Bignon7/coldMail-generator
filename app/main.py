import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text




def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Mail Generator")

    url_input = st.text_input("Enter a URL: ", value="https://careers.nike.com/fr/retail-associate-pt-nike-staten-island-14-29-hours-week/job/R-79939")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            st.code("Hello Hiring Manager, I am from AtliQ", language="markdown")

        except Exception as e:
            print("Lala is kind")