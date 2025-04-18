import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to handle missing values
def handle_missing_values(df):
    df = df.fillna(df.mean())
    return df

# Function to handle duplicate values
def handle_duplicate_values(df):
    df = df.drop_duplicates()
    return df


# Function to perform EDA
def perform_eda(df):
    st.write("## Exploratory Data Analysis")
    st.write("### Data Preview")
    st.write(df.head())

    st.write("### Data Description")
    st.write(df.describe())

    st.write("### Correlation Heatmap")
    corr = df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, ax=ax)
    st.pyplot(fig)
