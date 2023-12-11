import streamlit as st
import pandas as pd
from views import View

class MinhasConsultasUI:
  def main():
    st.header("Minhas Consultas")
    MinhasConsultasUI.listar()

  def listar():
    st.write("Código a programar")