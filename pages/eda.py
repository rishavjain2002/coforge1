import streamlit as st

st.set_page_config(
    layout='centered',
    page_title='DataHarbour'
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

def show1(df):     
    if df is not None and not df.empty:
        st.markdown(
        '<h1 class="centered-title">CSV Data Analysis and Model Evaluation</h1>',
        unsafe_allow_html=True
        )
        st.write(df.head())
    else:
        st.warning("The DataFrame is empty or invalid.")
