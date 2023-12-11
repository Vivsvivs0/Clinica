import streamlit as st
import pandas as pd
from views import View

class ConsultasMesUI:
  def main():
    st.header("Consultas do Mês")
    ConsultasMesUI.listar()

  def listar():
    st.write("nada ainda")