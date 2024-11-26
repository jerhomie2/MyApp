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
    input_age = st.slider('Age', min_value=27, max_value=59, value=(40,50))
    df1 = df[(df['Age'] >= input_age[0]) & (df['Age'] <= input_age[1])].copy()
    avg_sleep_duration = df1.groupby('Age')['Sleep Duration'].mean().reset_index()
    fig1 = px.bar(avg_sleep_duration, x='Age', y='Sleep Duration', title='Sleep Duration by Age')
    st.plotly_chart(fig1)

with tab2:
    st.header("Demographic Overview")
    gender_count = df['Gender'].value_counts()
    fig2 = px.pie(names=gender_count.index, values=gender_count.values, title="Gender Distribution")
    st.plotly_chart(fig2)