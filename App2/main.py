import streamlit as st
import pandas

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title('Liam Lin')
    content = """
    Hey, this is Liam, highly motivated Computer Science graduate student with a strong data analytics 
    and finance background (7 more years of working experience in private equity and stock market). 
    I am actively looking for 2024 software engineer intership/co-op opportunity.
    """
    st.info(content)

content2 = """
Below you can find some of the Apps I have built in Python.
Feel free to contact me :)
"""

st.write(content2)
col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])

