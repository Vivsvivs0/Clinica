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
        if len(View.consulta_listar()) > 0:
            dic = []
            for obj in View.consulta_listar(): dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhuma consulta cadastrada")
    def inserir():
        data = st.text_input("Data da consulta DD/MM/AAAA HH\:MM")
        medico = st.selectbox("Medico", View.medico_listar())
        paciente = st.selectbox("Paciente", View.paciente_listar())
        if st.button("Inserir"):
             View.consulta_inserir(data, True, paciente.get_id(), medico.get_id())
             st.success("Consulta inserida com sucesso")
    def atualizar():
        consulta = View.consulta_listar()
        if len(consulta) == 0:
            st.write("Nenhuma consulta cadastrada")
        else:
            op = st.selectbox("Atualização de consulta", consulta)
            data = st.text_input("Nova data da consulta DD/MM/AAAA HH\:MM")
            medico = st.selectbox("Novo medico", View.medico_listar())
            paciente = st.selectbox("Novo paciente", View.paciente_listar())
            if st.button("Atualizar"):
                View.consulta_atualizar(op.get_id(), data, True, paciente.get_id(), medico.get_id())
                st.success("Consulta atualizada com sucesso")
    def excluir():
        op = st.selectbox("Exclusão de horários", View.consulta_listar())
        if st.button("Excluir"):
            View.consulta_excluir(op.get_id())
            st.success("Consulta excluída com sucesso")