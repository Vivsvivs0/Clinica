import streamlit as st
import pandas as pd
from views import View

class RemarcarConsultaUI:
  def main():
    st.header("Remarcar consulta")
    RemarcarConsultaUI.remarcar()

  def remarcar():
    horarios = View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["paciente_id"]))
    if len(horarios) == 0:
      st.write("Você não possui nenhuma consulta marcada")
    else:  
      dic = []
      id = st.session_state["paciente_id"]
      for obj in horarios:
        if obj.get_id_paciente() == id:
          dic.append(obj._dict_)
      df = pd.DataFrame(dic)
      st.dataframe(df)
      horario = st.selectbox("Escolha a consulta a ser remarcada", horarios)
      newhorario = st.text_input("Informe a data desejada no formato dd/mm/aaaa HH\:MM")
      if st.button("Remarcar"):
          View.agenda_atualizar(horario.get_id(), False, newhorario, horario.get_id_medico(), horario.get_id_paciente())
          st.success("Solicitação de troca realizada com sucesso")
          st.rerun()