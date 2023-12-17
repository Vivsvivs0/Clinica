import streamlit as st
import pandas as pd
from views import View

class MinhasConsultasUI:
  def main():
    st.header("Minhas Consultas")
    MinhasConsultasUI.listar()

  def listar():
    if len(View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["paciente_id"]))) != 0:
      dic = []
      for obj in View.consulta_listar_paciente: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
    else:
      st.write("Você nao possui consultas marcadas")