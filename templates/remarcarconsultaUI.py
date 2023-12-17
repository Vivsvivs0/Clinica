import streamlit as st
import pandas as pd
from views import View

class RemarcarConsultaUI:
  def main():
    st.header("Remarcar Consulta")
    RemarcarConsultaUI.remarcar()

  def remarcar():
    st.write("lista das consultas da pessoa aqui")
    consulta = st.selectbox("Consulta escolhida", View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["paciente_id"])))
    data = st.text_input("Nova data DD/MM/AAAA HH:MM")
    if st.button("Remarcar"):
      st.write("nada ainda")