import streamlit as st
import pandas




# noinspection PyArgumentList
df=pandas.read_csv("data.csv")


st.header("The best company")


st.subheader("our team")

st.write("""
lorem ipsum dolor sit amet, consectetur adipiscing elit.""")

col1,col2,col3=st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.image("images/" + row["image"])


with col2:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.image("images/" + row["image"])

with col3:
    for index, row in df[4:].iterrows():
        st.subheader(f'{row["first name"].title()}{row["last name"].title()}')
        st.image("images/" + row["image"])
