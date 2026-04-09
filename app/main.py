import streamlit as st



st.title("Cold Mail Generator")

url_input = st.text_input("Enter a URL: ", value="https://careers.nike.com/fr/retail-associate-pt-nike-staten-island-14-29-hours-week/job/R-79939")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, I am from AtliQ", language="markdown")