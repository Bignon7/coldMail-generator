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
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extractçjobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language="markdown")

        except Exception as e:
            print("Lala is kind")









if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon=":email:")
    create_streamlit_app(chain, portfolio, clean_text)