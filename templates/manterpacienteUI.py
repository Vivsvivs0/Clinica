import streamlit as st
import pandas as pd
from views import View

class ManterPacienteUI:
    def main():
        st.header("Manter Paciente")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPacienteUI.listar()
        with tab2: ManterPacienteUI.inserir()
        with tab3: ManterPacienteUI.atualizar()
        with tab4: ManterPacienteUI.excluir()
    def listar():
        st.write("nada ainda")
    def inserir():
        st.write("nada ainda")
    def atualizar():
        st.write("nada ainda")
    def excluir():
        st.write("nada ainda")