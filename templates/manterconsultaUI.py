import streamlit as st
import pandas as pd
from views import View
import datetime

class ManterConsultaUI:
    def main():
        st.header("Manter Consulta")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterConsultaUI.listar()
        with tab2: ManterConsultaUI.inserir()
        with tab3: ManterConsultaUI.atualizar()
        with tab4: ManterConsultaUI.excluir()
    def listar():
        st.write("nada ainda")
    def inserir():
        st.write("nada ainda")
    def atualizar():
        st.write("nada ainda")
    def excluir():
        st.write("nada ainda")