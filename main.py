import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, empty_col, col2 = st.columns([1,1.5,1])

with col1:
    st.image("images/gee_profile.jpg")

with col2:
    st.title("Abdulganiyu Abubakar")
    content = """
    Hi, I am Abdulganiyu! I am a Software Engineer, teacher and the founder of GsureTech. 
    I graduated in 2019 with a Bachelor Degree in Computer Science from Bayero University Kano in Nigeria. I have worked with companies from various states, 
    such as Maritime Academy as a System Analyst, Hardcore Biometrics as a Software Engineer
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)

col3, col4 = st.columns(2)



