import streamlit as st

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
    st.write(content)