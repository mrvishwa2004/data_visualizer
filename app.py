import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Data Visualizer",
                   layout="centered",
                   page_icon="📊")

st.title("Data Visualizer - web app")
working_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = working_dir

files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

selected_file = st.selectbox("select the file" , files_list, index=None)

if selected_file:
    file_path = os.path.join(folder_path,selected_file)
    
    df = pd.read_csv(file_path)
    co1, co2 = st.columns(2)
    
    columns = df.columns.tolist()
    
    with co1:
        st.write("")
        st.write(df.head())
    
    with co2:
        x_axis = st.selectbox("select the X-Axis", options=columns + ["None"])
        y_axis = st.selectbox("select the Y-Axis", options=columns + ["None"])
        
        plot_list = ["Line plot","Bar chart","Scatter plot ","Count plot"]
        
        selected_plot = st.selectbox("Select the plot", options=plot_list, index=None)
        st.write(x_axis)
        st.write(y_axis)
        st.write(selected_plot)
        
    if st.button("Generate plot"):
        fig, ax = plt.subplots(figsize=(6,4))
        
        if selected_plot == 'Line Plot':
            sns.lineplot(x=df[x_axis],y=df[y_axis], ax=ax)
            
        elif selected_plot == 'Bar chart':
            sns.barplot(x=df[x_axis],y=df[y_axis], ax=ax)
            
        elif selected_plot == 'Scatter plot':
            sns.scatterplot(x=df[x_axis],y=df[y_axis], ax=ax)
        
        elif selected_plot == 'Count plot':
            sns.countplot(x=df[x_axis], ax=ax)
        
        
        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)
        
        plt.title(f"selected plot of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=12)
        plt.ylabel(y_axis, fontsize=12)
        
        st.pyplot(fig)
        
    