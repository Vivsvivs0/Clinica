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
        if len(View.paciente_listar()) > 0:
            dic = []
            for obj in View.paciente_listar(): dic.append(obj._dict_)
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhum paciente cadastrado")
    def inserir():
        nome = st.text_input("Nome do paciente")
        fone = st.text_input("Fone do paciente")
        email = st.text_input("Email do paciente")
        senha = st.text_input("Senha do paciente")
        if st.button("Inserir"):
             st.write("nada ainda")
    def atualizar():
        nome = st.text_input("Novo nome do paciente")
        fone = st.text_input("Novo fone do paciente")
        email = st.text_input("Novo email do paciente")
        senha = st.text_input("Nova senha do paciente")
        if st.button("Atualizar"):
            st.write("nada ainda")
    def excluir():
        op = st.selectbox("Exclusão de pacientes", View.paciente_listar())
        if st.button("Excluir"):
            st.write("nada ainda")