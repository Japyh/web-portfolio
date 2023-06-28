import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/AI.png", width=500)

with col2:
    st.title("Derya Umut Kulali")
    content ="""
    Hi, I am Derya Umut! I'm a student. My department is Electrical and Electronic Engineering. I am interested in AI.
    I am proficient in English, Pyhton, SQL and STM32. My hobbies include reading, writing and photography. I am working on artificial intelligence.
    """
    st.info(content)

content2 = "**Below you can find some of the apps I have built in Python. Feel free to contact me!**"
st.markdown(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")



with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

