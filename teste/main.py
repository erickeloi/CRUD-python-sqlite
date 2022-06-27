import streamlit as st
import requests
import backoff
import json 

import pandas as pd

import xlsxwriter
from io import BytesIO

from busca_na_api import *

def homepage():
    st.header("Bem vindo ao DashCounting app!")
    st.write("Escolha uma página acima ")

def search_info_predef_cnpj():
    st.header("Buscando informações dos CNPJ's de teste...")
    st.subheader("17895646000187, 18033552000161, 1365284000104\n")
    CNPJS = [17895646000187, 18033552000161, 1365284000104]
    st.write("---")
    for cnpj in CNPJS:
        data = get_api_info(cnpj)
        st.write(data)
        st.write(f"--- Fim da Ficha do CNPJ: {cnpj} ---\n\n")

def search_info_new_cnpj():
    st.header("Busca por CNPJ: ")

    cnpj = st.number_input(
        "Digite o CNPJ, somente números: ",
        step = 0
    )
    pesquisar = st.button("Pesquisar")
    if pesquisar:
        st.write("Procurando o CNPJ desejado...")
        st.write(get_api_info(cnpj))

def search_and_download():
    cnpj = st.number_input(
        "Digite o CNPJ, somente números: ",
        step = 0
    )
    pesquisar = st.button("Pesquisar")
    if pesquisar:
        st.write("Procurando o CNPJ desejado...")
        cnpj_info = get_api_info(cnpj)

        st.write(cnpj_info)

        st.write("Busca concluida! ")

        st.write("Convertendo informações para excel...")
        output = BytesIO()

        # Write files to in-memory strings using BytesIO
        # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()
        
        worksheet.write('A1', 'Hello')  
        workbook.close()

        st.download_button(
            label = "Download Excel workbook",
            data = output.getvalue(),
            file_name = "workbook.xlsx",
            mime = "application/vnd.ms-excel"
        )

pages = {"Homepage": homepage,
"Buscar informações dos CNPJ's padrões": search_info_predef_cnpj,
"Buscar informações de um novo CNPJ": search_info_new_cnpj,
"Buscar empresa e baixar informações dela em Excel": search_and_download
}

select_page = st.selectbox(
    "Escolha a Página",
    pages.keys()
)

pages[select_page]()

