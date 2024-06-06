import streamlit as st

st.header('Contact ME')

with st.form(key='email_forms'):
    user_email = st.text_input('your email address')
    message = st.text_area('Your message')
    button = st.form_submit_button()

    if button: