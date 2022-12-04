#Rodrigo Hernández A01610903
#Nadia Luna Rivas A01658134
# Carlos Ledezma A00828114 


#-----------Libreiras
import streamlit as st
import pandas as pd
import numpy as np

#-----------Constantes y dtos
nameC = "movies.csv"
nrowsC = 1000

sidebar = st.sidebar
titleS = 'Buscar peliculas'
descript = '¡Busca peliculas usando el filtro que prefieras!'

DesFil1 = 'Buscar filmes por tituulo'
DesFil2 = 'Buscar filmes por director'


#-----------Variables

#-----------Funciones
@st.cache(suppress_st_warning=True)
def showDataset(name,nrows):
    df=pd.read_csv(name,nrows=nrows)
    dfvis = df.copy()
    return df, dfvis

df, dfvis= showDataset(nameC,nrowsC)


def filter_data_by_filme(filme):
    filtered_data_filme = df[df['name'].str.lower().str.contains(filme)]
    return filtered_data_filme

def filter_data_by_director(director):
    filtered_data_filme = df[df['director'].str.lower().str.contains(director)]
    return filtered_data_filme
#----------Sidebar
sidebar.title(titleS)
sidebar.header(descript)

#----------Web
titmov = sidebar.text_input(DesFil1)
if sidebar.button('Buscar'):
    dfvis = (filter_data_by_filme(str(titmov).lower()))

dirct_name = sidebar.selectbox(DesFil2,df['director'].unique())
if sidebar.button('Buscar Director'):
    dfvis = (filter_data_by_director(str(dirct_name).lower()))

if sidebar.checkbox('Visualizar Dataset?'):
    st.dataframe(dfvis)
    if dfvis.shape[0] == df.shape[0]:
        st.text('Sin filtros')
    else:
        st.text(f'Total de peliculas filtradas: {dfvis.shape[0]}')





