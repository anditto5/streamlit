import streamlit as st
import pandas as pd
import numpy as np
from utils import load_css

load_css()

st.title("Project Overview")
st.write("This page contains the overview of the project.")
st.write("Overview of the Insurance Claims Analysis Project"")


st.write("## Insurance Claims Data")
df = pd.read_csv("insurance_claims.csv")  # Assuming you have a CSV file with your projects
df.drop(["incident_hour_of_the_day",'insured_zip','policy_bind_date','incident_location'],axis=1,inplace=True)
st.write(df.head())  # Display the first few rows of the dataset

st.write("### Data Overview")
st.write("The dataset contains various features related to insurance claims, including policy details, incident information, and whether the claim was fraudulent or not. The goal is to analyze this data to uncover insights and trends.")
##Separating features and target variable
X = df.drop("fraud_reported", axis=1)
y = df["fraud_reported"]
st.write("### Features and Target Variable")
st.write("Features (X):", X.columns.tolist())
