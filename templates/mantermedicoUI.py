import streamlit as st
import pandas as pd
from views import View

class ManterMedicoUI:
    def main():
        st.header("Manter Medico")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterMedicoUI.listar()
        with tab2: ManterMedicoUI.inserir()
        with tab3: ManterMedicoUI.atualizar()
        with tab4: ManterMedicoUI.excluir()
    def listar():
        st.write("nada ainda")
    def inserir():
        st.write("nada ainda")
    def atualizar():
        st.write("nada ainda")
    def excluir():
        st.write("nada ainda")