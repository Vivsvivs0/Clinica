import streamlit as st
import pandas as pd
from views import View
import datetime

class SolicitarUI:
    def main():
        st.header("Solicitar consulta")
        SolicitarUI.solicitar()
    def solicitar():
        if len(View.medico_listar()) > 0:
            medico = st.selectbox("Médico desejado", View.medico_listar())
            data = st.text_input("Data em formato DD/MM/AAAA HH\:MM")
            if st.button("Solicitar"):
              if View.medico_disponivel(medico, data):
                data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.consulta_inserir(data, False, st.session_state["cliente_id"], medico.get_id())
                st.success("Consulta solicitada com sucesso, aguarde confirmação")
              else:
                 st.error("Médico ocupado no horário selecionado")
        else:
            st.write("Nenhum médico disponível para consultas")