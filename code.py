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

with st.sidebar:
    input_age = st.slider('Age Range', min_value=27, max_value=59, value=(40,50))
    input_gender = st.radio('Gender', ['Male','Female'])
    input_disorder = st.radio('Disorder', ['Sleep Apnea','Insomnia', 'None '])
    male_button = st.button('Male')
    female_button = st.button('Female')
    if male_button:
        input_gender = 'Male'
    elif female_button:
        input_gender = 'Female'
    else:
        input_gender = None  # No gender selected yet
    st.write(f"Selected Gender: {input_gender}")

tab1, tab2, tab3 = st.tabs(['Age','Gender','Sleep Disorder'])
with tab1:
    df1 = df[(df['Age'] >= input_age[0]) & (df['Age'] <= input_age[1])].copy()
    avg_sleep_duration = df1.groupby('Age')['Sleep Duration'].mean().reset_index()
    fig1 = px.bar(avg_sleep_duration, x='Age', y='Sleep Duration', title='Average Sleep Duration by Age')
    st.plotly_chart(fig1)

with tab2:
    df1 = df[df['Gender'] == input_gender].copy()
    avg_sleep_duration = df1.groupby(['Gender','Age', 'BMI Category'])['Sleep Duration'].mean().reset_index()
    fig1 = px.line(avg_sleep_duration, x='Age', y='Sleep Duration', title='Average Sleep Duration by Gender and BMI Category', color = 'BMI Category')
    st.plotly_chart(fig1)

with tab3:
    df1 = df[df['Sleep Disorder'] == input_disorder].copy()
    avg_sleep_duration = df1.groupby(['Sleep Disorder','Age', 'Gender'])['Sleep Duration'].mean().reset_index()
    fig1 = px.bar(avg_sleep_duration, x='Age', y='Sleep Duration', title='Average Sleep Duration by Disorder', color = 'Gender', barmode='group')
    st.plotly_chart(fig1)