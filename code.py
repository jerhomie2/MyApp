import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('sleep.csv')

st.title('Sleep Data')

tab1, tab2 = st.tabs(['Age','Gender'])
with tab1:
    input_age = st.slider('Age', min_value=27, max_value=59, value=40)
    df1 = df[df['Age'] == input_age].copy()
    average_sleep_duration = df1['Sleep Duration'].mean()
    bar_data = pd.DataFrame({
        'Age': [input_age],
        'Average Sleep Duration': [average_sleep_duration]
    })
    fig1 = px.bar(df, x='Age', y='Average Sleep Duration', title='Average Sleep Duration by Age')
    st.plotly_chart(fig1)

with tab2:
    st.header("Demographic Overview")
    gender_count = df['Gender'].value_counts()
    fig2 = px.pie(names=gender_count.index, values=gender_count.values, title="Gender Distribution")
    st.plotly_chart(fig2)