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
        if len(View.medico_listar()) > 0:
            dic = []
            for obj in View.medico_listar(): dic.append(obj._dict_)
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhum médico cadastrado")    
    def inserir():
        nome = st.text_input("Nome do médico")
        fone = st.text_input("Fone do médico")
        email = st.text_input("Email do médico")
        if st.button("Inserir"):
             st.write("nada ainda")
    def atualizar():
        nome = st.text_input("Novo nome do médico")
        fone = st.text_input("Novo fone do médico")
        email = st.text_input("Novo email do médico")
        if st.button("Atualizar"):
            st.write("nada ainda")
    def excluir():
        op = st.selectbox("Exclusão de médicos", View.medico_listar())
        if st.button("Excluir"):
            st.write("nada ainda")