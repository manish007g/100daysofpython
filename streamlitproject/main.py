import streamlit as st
import pandas as pd

st.write("""
#My First App
Hello *world!*
""")

df = pd.read_csv("/Users/91809/PycharmProjects/streamlitproject/Business.csv")
st.dataframe(df)