import streamlit as st
import pandas as pd
from views import View

class ConfirmarConsultaUI:
  def main():
    st.header("Confirmar Consulta")
    ConfirmarConsultaUI.confirmar()

  def confirmar():
    if len(View.consulta_nao_confirmada()) != 0:
      dic = []
      for obj in View.consulta_nao_confirmada: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
    else:
      st.write("Não há consultas não confirmadas")
    consulta = st.selectbox("Consulta escolhida", View.consulta_nao_confirmada())
    if st.button("Confirmar"):
      View.consulta_atualizar(consulta.get_id(), consulta.get_data(), True, consulta.get_id_paciente(), consulta.get_id_medico())
      st.success("Consulta confirmada com sucesso")