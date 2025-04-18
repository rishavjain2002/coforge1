import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pages.overview as overview
import pages.eda as eda
import data

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

st.markdown(
    '<h1 class="centered-title">CSV Data Analysis and Model Evaluation</h1>',
    unsafe_allow_html=True
)
uploaded_file = st.file_uploader(label='Upload your dataset:')
    
if uploaded_file is not None:
    df_main = pd.read_csv(uploaded_file)
    st.session_state.df_main = df_main
    feature_columns = df_main.columns.tolist()
    type_options = ['Regression', 'Classification']
    with st.container():
        col1, col2 = st.columns(2)

        with col2:
            target_column = st.selectbox("Select the target column", feature_columns,index = None)
        with col1:
            target_type = st.selectbox("Type of dataset", type_options, index = None)       
                      
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['Upload','EDA', 'Model Evaluation'],
        icons=['book','bar-chart', 'robot'],
        orientation='horizontal'
    )

if selected == 'Upload':
    if 'df_main' in st.session_state and st.session_state.df_main is not None and not st.session_state.df_main.empty:
        df = overview.show(st.session_state.df_main)
        df = data.handle_missing_values(df)
        df = data.handle_duplicate_values(df)
        st.session_state.df = df

        
if selected == 'EDA':
    if 'df' in st.session_state and st.session_state.df is not None and not st.session_state.df.empty:
        eda.show1(st.session_state.df)
        st.session_state.df = pd.DataFrame()
    else:
        st.warning("Please upload a dataset first.")
    
    
