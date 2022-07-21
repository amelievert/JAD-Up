# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pip install streamlit
import streamlit as st


st.sidebar.title("Sommaire")

pages = ["Introduction au jeu de données",
         "Analyse",
         "Preprocessing",
         "Challenge de modèles",
         "Pour aller plus loin"]

page = st.sidebar.radio("Aller vers", pages)