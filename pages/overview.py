import streamlit as st
import pandas as pd
import data
    
def show(df):
    if df is not None and not df.empty:
        st.write("---")
        with st.container():
            st.markdown("<h2 style='text-align: center'>Feature Types</h2>", unsafe_allow_html=True)

        object_type = df.select_dtypes(include=['object']).columns.tolist()
        numeric_type = df.select_dtypes(include=['int64', 'int32']).columns.tolist()

        with st.container():
            col3, col4 = st.columns(2)

            with col3:
                st.subheader("Categorical Features")
                for col in object_type:
                    st.write(f"- {col}")

            with col4:
                st.subheader("Numerical Features")
                for col in numeric_type:
                    st.write(f"- {col}")

        df = data.handle_missing_values(df)
        df = data.handle_duplicate_values(df)
        
        return df
    else:
        return None
    