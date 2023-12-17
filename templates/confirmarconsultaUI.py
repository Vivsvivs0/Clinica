import streamlit as st
import pandas as pd
from views import View

class ConfirmarConsultaUI:
  def main():
    st.header("Confirmar Consulta")
    ConfirmarConsultaUI.confirmar()

  def confirmar():
    st.write("lista das consultas nao confirmadas")
    consulta = st.selectbox("Consulta escolhida", View.consulta_nao_confirmada())
    if st.button("Confirmar"):
      st.write("nada ainda")