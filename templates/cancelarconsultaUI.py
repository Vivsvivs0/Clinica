import streamlit as st
import pandas as pd
from views import View

class CancelarConsultaUI:
  def main():
    st.header("Cancelar Consulta")
    CancelarConsultaUI.cancelar()

  def cancelar():
    st.write("lista das consultas da pessoa aqui")
    consulta = st.selectbox("Consulta escolhida", View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["paciente_id"])))
    if st.button("Cancelar"):
      st.write("nada ainda")