import streamlit as st
from views import View

class SolicitarConsultaUI:
  def main():
    st.header("Solicitar Consulta")
    SolicitarConsultaUI.solicitar()

  def solicitar():
    medico = st.selectbox("Médico escolhido", View.medico_listar())
    data = st.text_input("Data DD/MM/AAAA HH\:MM")
    if st.button("Solicitar"):
      st.write("nada ainda")