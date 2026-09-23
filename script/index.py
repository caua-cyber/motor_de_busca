import streamlit as lt

def header():
    titulo = lt.title("Motor de busca financeiro")
    
    return titulo

def selector():
    entrada = lt.text_input("informe a ação ou ativo:" , placeholder="infome:")
    button = lt.button("Procurar")
    return entrada

header()
selector()