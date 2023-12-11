import streamlit as st
import pandas as pd
from views import View

class CancelarConsultaUI:
  def main():
    st.header("Cancelar Consulta")
    CancelarConsultaUI.cancelar()

  def cancelar():
    st.write("Código a programar")