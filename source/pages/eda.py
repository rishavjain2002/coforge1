import streamlit as st

# st.set_page_config(
#     layout='centered',
#     page_title='DataHarbour'
# )

st.markdown(
    """
    <style>
        .centered-title {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)
def show1(df):     
    if df is not None and not df.empty:
        st.markdown(
        '<h1 class="centered-title">CSV Data Analysis and Model Evaluation</h1>',
        unsafe_allow_html=True
        )
        st.write(df.head())
    else:
        st.warning("The DataFrame is empty or invalid.")
